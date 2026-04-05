import pandas as pd
import numpy as np
import time
import logging
import os
import tempfile
import random
from collections import defaultdict
from itertools import combinations
from typing import List, Dict, Tuple, Optional, Set
from scipy.sparse import csr_matrix

# Configuración de logging senior
logger = logging.getLogger(__name__)

# Importe dinámico de R para habilitar el modo híbrido solo si R está presente
try:
    import rpy2.robjects as robjects
    from rpy2.robjects.packages import importr
    R_AVAILABLE = True
except ImportError:
    R_AVAILABLE = False
    logger.warning("Motor R (rpy2) no detectado. El modo híbrido no estará disponible.")

class AprioriHybridEngine:
    """
    Motor de reglas de asociación que combina una implementación manual en Python 
    con el motor arules de R para máximo rendimiento.
    """
    def __init__(self, transactions: List[List[str]]):
        self.transactions = transactions
        self.itemsets: Dict[int, List[List[str]]] = {}
        self.rules = pd.DataFrame()
        self.support_dict: Dict[Tuple[str, ...], float] = {}

    def _generar_candidatos(self, itemsets_frecuentes_k: List[List[str]], k: int, max_candidates: int = 100000) -> List[List[str]]:
        """
        Genera candidatos (k+1)-itemsets a partir de itemsets frecuentes de tamaño k.
        """
        n = len(itemsets_frecuentes_k)
        if n == 0: return []
        
        # Limitar itemsets si son demasiados para evitar explosión combinatoria
        if n > 1000:
            logger.info(f"Limitando itemsets de tamaño {k} a los 1000 más frecuentes para generación.")
            itemsets_frecuentes_k = sorted(
                itemsets_frecuentes_k, 
                key=lambda x: self.support_dict.get(tuple(sorted(x)), 0), 
                reverse=True
            )[:1000]
            n = 1000

        candidatos_set = set()
        if k == 1:
            for i in range(n):
                for j in range(i+1, n):
                    candidato = tuple(sorted([itemsets_frecuentes_k[i][0], itemsets_frecuentes_k[j][0]]))
                    candidatos_set.add(candidato)
        else:
            # Índice por prefijo para eficiencia (k-1 elementos iguales)
            prefix_index = {}
            for idx, itemset in enumerate(itemsets_frecuentes_k):
                prefix = tuple(sorted(itemset[:k-1]))
                prefix_index.setdefault(prefix, []).append(idx)
            
            for prefix, indices in prefix_index.items():
                for i in range(len(indices)):
                    for j in range(i+1, len(indices)):
                        idx1, idx2 = indices[i], indices[j]
                        new_item = itemsets_frecuentes_k[idx2][k-1]
                        candidato = tuple(sorted(list(prefix) + [itemsets_frecuentes_k[idx1][k-1], new_item]))
                        candidatos_set.add(candidato)

        result = [list(x) for x in candidatos_set]
        return result[:max_candidates]

    def _poda_apriori(self, candidatos: List[List[str]], itemsets_frecuentes_k: List[List[str]], k: int) -> List[List[str]]:
        """
        Elimina candidatos cuyos subconjuntos de tamaño k no son frecuentes.
        """
        frecuentes_set = set(tuple(sorted(x)) for x in itemsets_frecuentes_k)
        podados = []
        for cand in candidatos:
            subset_frecuente = True
            for i in range(len(cand)):
                sub = tuple(sorted(cand[:i] + cand[i+1:]))
                if sub not in frecuentes_set:
                    subset_frecuente = False
                    break
            if subset_frecuente:
                podados.append(cand)
        return podados

    def run_python_manual(self, min_support: float = 0.01, min_confidence: float = 0.3, batch_size: int = 50000):
        """
        Implementación manual optimizada con procesamiento por lotes para ahorro de memoria.
        """
        n_total = len(self.transactions)
        logger.info(f"Iniciando Apriori Manual (Soporte: {min_support}, Confianza: {min_confidence})")
        
        # Fase 1: 1-itemsets
        item_counts = {}
        for trans in self.transactions:
            for item in trans:
                item_counts[item] = item_counts.get(item, 0) + 1
        
        frequent_1 = [[item] for item, count in item_counts.items() if count/n_total >= min_support]
        self.itemsets[1] = frequent_1
        for item, count in item_counts.items():
            if count/n_total >= min_support:
                self.support_dict[tuple([item])] = count/n_total
        
        logger.info(f"Encontrados {len(frequent_1)} 1-itemsets frecuentes.")

        k = 1
        while self.itemsets.get(k, []):
            logger.info(f"Generando {k+1}-itemsets...")
            candidatos = self._generar_candidatos(self.itemsets[k], k)
            candidatos_podados = self._poda_apriori(candidatos, self.itemsets[k], k)
            
            if not candidatos_podados:
                break
                
            # Conteo por lotes
            counts = {tuple(sorted(c)): 0 for c in candidatos_podados}
            for i in range(0, n_total, batch_size):
                batch = self.transactions[i:i + batch_size]
                for trans in batch:
                    trans_set = set(trans)
                    for cand in candidatos_podados:
                        if all(item in trans_set for item in cand):
                            counts[tuple(sorted(cand))] += 1
            
            frequent_k_plus_1 = [list(c) for c, count in counts.items() if count/n_total >= min_support]
            for c, count in counts.items():
                if count/n_total >= min_support:
                    self.support_dict[c] = count/n_total
            
            if not frequent_k_plus_1:
                break
            
            k += 1
            self.itemsets[k] = frequent_k_plus_1
            logger.info(f"Encontrados {len(frequent_k_plus_1)} {k}-itemsets frecuentes.")

        self._generar_reglas_python(min_confidence)
        return self.rules

    def _generar_reglas_python(self, min_confidence: float):
        """
        Genera reglas de asociación a partir de los itemsets frecuentes encontrados.
        """
        rules_list = []
        for k, itemsets in self.itemsets.items():
            if k < 2: continue
            for itemset in itemsets:
                itemset_tuple = tuple(sorted(itemset))
                support_all = self.support_dict.get(itemset_tuple, 0)
                
                for i in range(1, k):
                    for ant_tuple in combinations(itemset, i):
                        ant = list(ant_tuple)
                        cons = [item for item in itemset if item not in ant]
                        
                        support_ant = self.support_dict.get(tuple(sorted(ant)), 0)
                        if support_ant == 0: continue
                        
                        confidence = support_all / support_ant
                        if confidence >= min_confidence:
                            support_cons = self.support_dict.get(tuple(sorted(cons)), 0)
                            lift = confidence / support_cons if support_cons > 0 else 0
                            rules_list.append({
                                'antecedent': ant,
                                'consequent': cons,
                                'support': support_all,
                                'confidence': confidence,
                                'lift': lift
                            })
        
        self.rules = pd.DataFrame(rules_list)
        if not self.rules.empty:
            self.rules.sort_values('lift', ascending=False, inplace=True)
            self.rules.reset_index(drop=True, inplace=True)

    def run_r_hybrid(self, min_support: float = 0.001, min_confidence: float = 0.3):
        """
        Ejecuta el motor arules de R mediante un archivo temporal compartido.
        """
        if not R_AVAILABLE:
            logger.error("R (rpy2) no está disponible. Fallback planeado.")
            return self.run_python_manual(min_support, min_confidence)
        
        logger.info("Iniciando Motor Híbrido R (arules)...")
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8') as tmp:
            for trans in self.transactions:
                tmp.write(",".join(trans) + "\n")
            tmp_path = tmp.name.replace("\\", "/")

        try:
            # Ejecución en R
            robjects.r(f'''
                if (!require("arules")) install.packages("arules", repos="http://cran.us.r-project.org")
                library(arules)
                baskets <- read.transactions("{tmp_path}", sep = ",", format = "basket")
                rules_r <- apriori(baskets, parameter = list(support = {min_support}, confidence = {min_confidence}, minlen = 2))
                df <- as(rules_r, "data.frame")
            ''')
            
            rules_df = robjects.globalenv['df']
            # Convertir R Dataframe a Pandas (vía bridge manual para evitar dependencias extra)
            # arules reporta rules como "{A} => {B}"
            self.rules = pd.DataFrame({
                'rules': list(rules_df.rx2('rules')),
                'support': list(rules_df.rx2('support')),
                'confidence': list(rules_df.rx2('confidence')),
                'lift': list(rules_df.rx2('lift'))
            })
            
            # Limpiar y formatear para visualista
            self.rules['antecedent'] = self.rules['rules'].apply(lambda x: x.split(" => ")[0].strip("{}").split(","))
            self.rules['consequent'] = self.rules['rules'].apply(lambda x: x.split(" => ")[1].strip("{}").split(","))
            self.rules.drop(columns=['rules'], inplace=True)
            self.rules.sort_values('lift', ascending=False, inplace=True)
            
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
                
        return self.rules

    def get_recommendations(self, basket: List[str], top_n: int = 5, match_threshold: float = 0.5) -> pd.DataFrame:
        """
        Genera sugerencias basadas en un basket de entrada comparado con las reglas generadas.
        """
        if self.rules.empty:
            logger.warning("No hay reglas generadas para realizar recomendaciones.")
            return pd.DataFrame()
        
        recommendations = []
        basket_set = set(basket)
        
        for _, rule in self.rules.iterrows():
            ant_set = set(rule['antecedent'])
            if not ant_set: continue
            
            # Coincidencia parcial (Senior Logic)
            intersection = ant_set.intersection(basket_set)
            match_score = len(intersection) / len(ant_set)
            
            if match_score >= match_threshold:
                # Evitar recomendar algo que ya está en el basket
                cons_filtered = [item for item in rule['consequent'] if item not in basket_set]
                if cons_filtered:
                    recommendations.append({
                        'product': ", ".join(cons_filtered),
                        'confidence': rule['confidence'],
                        'lift': rule['lift'],
                        'match_score': match_score
                    })
        
        df_rec = pd.DataFrame(recommendations)
        if not df_rec.empty:
            return df_rec.sort_values(['match_score', 'lift'], ascending=False).head(top_n)
        return pd.DataFrame()
    @staticmethod
    def generate_synthetic_data(n_transactions: int, n_items: int, avg_length: int) -> List[List[str]]:
        """
        Genera un dataset sintético para pruebas de complejidad y rendimiento.
        """
        items = [f'item_{i}' for i in range(n_items)]
        transactions = []
        for _ in range(n_transactions):
            length = max(1, int(np.random.normal(avg_length, avg_length/4)))
            length = min(length, n_items)
            transactions.append(random.sample(items, length))
        return transactions

    def run_brute_force(self, min_support: float = 0.5, max_length: Optional[int] = None) -> Dict[frozenset, int]:
        """
        Implementación por fuerza bruta (sin poda) para propósitos comparativos.
        ADVERTENCIA: Muy lento en datasets reales.
        """
        transactions_sets = [set(t) for t in self.transactions]
        n_total = len(self.transactions)
        min_count = min_support * n_total
        
        all_items = set()
        for t in self.transactions:
            all_items.update(t)
            
        if max_length is None:
            max_length = len(all_items)
            
        frequent_itemsets = {}
        for k in range(1, max_length + 1):
            candidates = list(combinations(all_items, k))
            found_any = False
            for cand in candidates:
                cand_set = frozenset(cand)
                count = sum(1 for t in transactions_sets if cand_set.issubset(t))
                if count >= min_count:
                    frequent_itemsets[cand_set] = count
                    found_any = True
            if not found_any:
                break
        return frequent_itemsets

def benchmark_engines(datasets: Dict[str, List[List[str]]], min_supports: List[float]):
    """
    Compara el rendimiento de diferentes implementaciones de Apriori.
    """
    results = defaultdict(list)
    for name, data in datasets.items():
        engine = AprioriHybridEngine(data)
        for sup in min_supports:
            # Test Manual Python
            start = time.time()
            engine.run_python_manual(min_support=sup)
            results['Python Manual'].append({'dataset': name, 'support': sup, 'time': time.time() - start})
            
            # Test R (if available)
            if R_AVAILABLE:
                start = time.time()
                engine.run_r_hybrid(min_support=sup)
                results['R Hybrid'].append({'dataset': name, 'support': sup, 'time': time.time() - start})
    return results

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Dummy test
    dummy_data = [["leche", "pan", "huevos"], ["pan", "huevos"], ["leche", "manzana"]]
    engine = AprioriHybridEngine(dummy_data)
    rules = engine.run_python_manual(min_support=0.01)
    print(rules)
