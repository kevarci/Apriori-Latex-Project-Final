import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from scipy.sparse import csr_matrix
import time

products = pd.read_csv('order_products__train.csv')
orders = pd.read_csv('products.csv')

dfMerged = pd.merge(orders, products, on="product_id", how="inner")

# Agrupar productos por transacción para crear listas de transacciones

transactions = dfMerged.groupby("order_id")["product_name"].apply(list).tolist()
print(f"Primeras transacciones:\n{transactions[:5]}")

item_mapping = {item: idx for idx, item in enumerate(sorted(set(item for transaction in transactions for item in transaction)))}
rows, cols = [], []
for row_idx, transaction in enumerate(transactions):
    for item in transaction:
        rows.append(row_idx)
        cols.append(item_mapping[item])

# Crear la matriz dispersa
order_matrix_sparse = csr_matrix(([1] * len(rows), (rows, cols)), shape=(len(transactions), len(item_mapping)))

# Función para calcular soporte de elementos individuales
def calculate_support(item_indices, data_matrix):
    
    item_mask = data_matrix[:, item_indices].toarray().all(axis=1)
    support = np.sum(item_mask) / data_matrix.shape[0]
    return support

# Función para generar ítems frecuentes utilizando matrices dispersas
def apriori_manual(data_matrix, min_support):
  
    num_items = data_matrix.shape[1]
    frequent_itemsets = []
    current_itemsets = [[i] for i in range(num_items)]
    
    while current_itemsets:
        next_itemsets = []
        item_supports = []
        
        # Calcular soporte para cada conjunto actual
        for itemset in current_itemsets:
            support = calculate_support(itemset, data_matrix)
            if support >= min_support:
                frequent_itemsets.append((itemset, support))
                item_supports.append(itemset)
        
        # Generar nuevas combinaciones de ítems frecuentes actuales
        for i in range(len(item_supports)):
            for j in range(i + 1, len(item_supports)):
                combined_itemset = sorted(set(item_supports[i]) | set(item_supports[j]))
                if len(combined_itemset) == len(item_supports[i]) + 1:
                    next_itemsets.append(combined_itemset)
        
        current_itemsets = next_itemsets  # Actualizar conjuntos actuales
    
    return frequent_itemsets

#Convertimos la matriz dispersa a una lista de listas 
def sparse_transaction(data_matrix, item_mapping):
    reverse_mapping = {idx: item for item, idx in item_mapping.items()}

    transactions = []
    #Aplicamos la función a cada fila de la matriz dispersa
    for i in range(data_matrix.shape[0]):
        #obtener indices de elementos no cero
        row = data_matrix[i]
        row_indices = row.indices
        
        # Convertir índices a nombres de productos usando el mapeo inverso
        transaction = []
        for idx in row_indices:
            if idx in reverse_mapping:
                transaction.append(reverse_mapping[idx])
            else:
                print(f"Advertencia: Índice {idx} no encontrado en el mapeo inverso")
        
        transactions.append(transaction)
    
    return transactions

# def generar_candidatos(itemsets_frecuentes_k, k,max_candidates= 100000):
    # if len(itemsets_frecuentes_k) > 1000:
    #     print(f"Demasiados itemsets frecuentes ({len(itemsets_frecuentes_k)}). Limitando a los 1000 más frecuentes.")
    #     # Aquí asumimos que los itemsets ya están ordenados por soporte
    #     itemsets_frecuentes_k = itemsets_frecuentes_k[:1000]
    # candidatos = []
    # n = len(itemsets_frecuentes_k)
    
    # # join => combinar itemsets que comparten k-1 elementos
    # for i in range(n):
    #     for j in range(i+1, n):
    #         # k=1 simplemente combinamos los items
    #         if k == 1:
    #             candidato = [itemsets_frecuentes_k[i][0], itemsets_frecuentes_k[j][0]]
    #             candidatos.append(sorted(candidato))
    #         else:
    #             # Para k>1 verificamos si los primeros k-1  son iguales
    #             if itemsets_frecuentes_k[i][:k-1] == itemsets_frecuentes_k[j][:k-1]:
    #                 # Combinamos
    #                 candidato = itemsets_frecuentes_k[i].copy()
    #                 candidato.append(itemsets_frecuentes_k[j][k-1])
    #                 candidato.sort()
    #                 candidatos.append(candidato)
    
    # # Eliminar duplicados usando un conjunto (set)
    # candidatos_unicos = [list(x) for x in set(tuple(x) for x in candidatos)]
    # return candidatos_unicos

def generar_candidatos(itemsets_frecuentes_k, k, max_candidates=100000, support_dict=None):
    # Limitar itemsets frecuentes si hay demasiados
    if len(itemsets_frecuentes_k) > 1000:
        print(f"Demasiados itemsets frecuentes ({len(itemsets_frecuentes_k)}). Limitando a los 1000 más frecuentes.")
        if support_dict:
            # Ordenar por soporte si tenemos el diccionario de soporte
            itemsets_frecuentes_k = sorted(itemsets_frecuentes_k, 
                                          key=lambda x: support_dict.get(tuple(x), 0), 
                                          reverse=True)[:1000]
        else:
            itemsets_frecuentes_k = itemsets_frecuentes_k[:1000]
    
    # Estimación del número de candidatos que se generarán
    n = len(itemsets_frecuentes_k)
    estimated_candidates = n * (n - 1) // 2
    
    # Si la estimación supera el máximo, aplicamos filtrado adicional
    if estimated_candidates > max_candidates:
        reduction_factor = max_candidates / estimated_candidates
        limit = int(n * reduction_factor**0.5)
        print(f"Estimación de candidatos ({estimated_candidates}) excede el máximo. Limitando a {limit} itemsets.")
        if support_dict:
            itemsets_frecuentes_k = sorted(itemsets_frecuentes_k, 
                                          key=lambda x: support_dict.get(tuple(x), 0), 
                                          reverse=True)[:limit]
        else:
            itemsets_frecuentes_k = itemsets_frecuentes_k[:limit]
        n = len(itemsets_frecuentes_k)
    
    # Usar un conjunto para evitar duplicados desde el principio
    candidatos_set = set()
    
    # Para k=1, usar un enfoque más eficiente
    if k == 1:
        for i in range(n):
            for j in range(i+1, n):
                candidato = tuple(sorted([itemsets_frecuentes_k[i][0], itemsets_frecuentes_k[j][0]]))
                candidatos_set.add(candidato)
    else:
        # Optimización: creo un índice para agrupar itemsets que comparten prefijo
        prefix_index = {}
        for idx, itemset in enumerate(itemsets_frecuentes_k):
            prefix = tuple(itemset[:k-1])
            if prefix not in prefix_index:
                prefix_index[prefix] = []
            prefix_index[prefix].append(idx)
        
        # Generar candidatos solo entre itemsets con el mismo prefijo
        for prefix, indices in prefix_index.items():
            if len(indices) > 1:  # Necesitamos al menos 2 itemsets con el mismo prefijo
                for i in range(len(indices)):
                    for j in range(i+1, len(indices)):
                        idx1, idx2 = indices[i], indices[j]
                        # Crear candidato
                        candidato = list(prefix) + [itemsets_frecuentes_k[idx1][k-1], itemsets_frecuentes_k[idx2][k-1]]
                        candidato.sort()
                        candidatos_set.add(tuple(candidato))
    
    # Convertir de vuelta a lista de listas
    candidatos_unicos = [list(x) for x in candidatos_set]
    
    # Verificar si aún tenemos demasiados candidatos
    if len(candidatos_unicos) > max_candidates:
        print(f"Aún hay demasiados candidatos ({len(candidatos_unicos)}). Limitando a {max_candidates}.")
        candidatos_unicos = candidatos_unicos[:max_candidates]
    
    return candidatos_unicos

def poda_apriori(candidatos, itemsets_frecuentes_k, k):
    # Convertir itemsets frecuentes a conjunto para búsqueda eficiente O
    itemsets_frecuentes_set = set(tuple(x) for x in itemsets_frecuentes_k)
    candidatos_podados = []
    
    for candidato in candidatos:
        es_valido = True
        
        # Generar todos los subconjuntos de tamaño k 
        for i in range(len(candidato)):
            subconjunto = candidato.copy()
            subconjunto.pop(i)
            
            # si algun subconunto no es frecuente , el candidato no puede ser frecuente
            if tuple(subconjunto) not in itemsets_frecuentes_set:
                es_valido = False
                break
        
        if es_valido:
            candidatos_podados.append(candidato)
    
    return candidatos_podados

#Implementacion manual dde priori con procesamiento por lotes
def apriori_lotes(transantions_list, min_support, batch_size= 50000):
    n_total = len(transactions_list)
    print(f"Procesando {n_total} transacciones con soporte minimo {min_support}")

    item_counts = {}

    n_batches = (n_total + batch_size - 1) // batch_size

    print('Fase 1: Generando 1-itemsets frecuentes')

    for i in range(n_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, n_total)
        print(f"Prosado lote {i + 1}/ {n_batches} (transacciones {start_idx}-{end_idx})")
        
        #transacciones para este lote
        batch_transactions = transactions_list[start_idx:end_idx]

        #contador
        for transaction in batch_transactions:
            for item in transaction:
                item_counts[item] = item_counts.get(item, 0) + 1

    #filtrado por soporte minimo
    frequent_1_itemsets = []
    support_dict = {}

    for item, count in item_counts.items():
        support = count / n_total
        if support >= min_support:
            frequent_1_itemsets.append([item])
            support_dict[tuple([item])] = support
    
    print(f"  Se encontraron {len(frequent_1_itemsets)} 1-itemsets frecuentes")

    all_frequent_itemsets = {1: frequent_1_itemsets}

    k = 1
    while all_frequent_itemsets.get(k, []):
        print(f"Fase {k + 1}: Generando {k + 1}-itemsets frecuentes")

        if len(all_frequent_itemsets[k]) > 1000:
            print(f"Demasiados itemsets frecuentes ({len(all_frequent_itemsets[k])}). Limitando a los 1000 con mayor soporte.")
           
            sorted_itemsets = sorted(all_frequent_itemsets[k], 
                                    key=lambda x: support_dict[tuple(x)], 
                                    reverse=True)[:1000]
            all_frequent_itemsets[k] = sorted_itemsets
            print(f"Limitado a {len(all_frequent_itemsets[k])} itemsets frecuentes")
        #generacion
        candidatos = generar_candidatos(all_frequent_itemsets[k], k)

        if len(candidatos) > 100000:
            print(f"¡Demasiados candidatos ({len(candidatos)})! Aumentando el umbral de soporte para esta fase.")
            # Aumentar temporalmente el umbral de soporte
            temp_min_support = min_support * 2
            print(f"Umbral de soporte temporal: {temp_min_support}")

            # Filtrar itemsets frecuentes con el nuevo umbral
            filtered_itemsets = []
            for itemset in all_frequent_itemsets[k]:
                if support_dict[tuple(itemset)] >= temp_min_support:
                    filtered_itemsets.append(itemset)
            
            print(f"Filtrando a {len(filtered_itemsets)} itemsets con mayor soporte")
            # Regenerar candidatos con el conjunto filtrado
            candidatos = generar_candidatos(filtered_itemsets, k)
            print(f"Nuevos candidatos generados: {len(candidatos)}")
    
        #aplicacion de poda
        candidatos_podados = poda_apriori(candidatos, all_frequent_itemsets[k], k)

        print(f"Generados {len(candidatos)} candidatos, {len(candidatos_podados)} despues de poda")

        if not candidatos_podados:
            break

    #dic para apariciones de candidatos
        candidato_counts = {tuple(c): 0 for c in candidatos_podados}
    
    #procesado poir lotes para contar candidatos
    for i in range(n_batches): 
        start = i * batch_size
        end_idx = min((i + 1) * batch_size, n_total)

        print(f"Procesando lote {i+1}/{n_batches} (transacciones {start_idx}={end_idx})")

        batch_transactions = transactions_list[start_idx:end_idx]
        
        #volvemos a contar los candidatos de este lote
        for transaction in batch_transactions:
            trasactions_set = set(transaction)
            for candidato in candidatos_podados:
                #aqui verificamos que los candidatos esten
                if all(item in transaction_set for item in candidato):
                    candidato_counts[tuple(candidato)] += 1

        frequent_itemsets_k_plus_1 = []
        
        for candidato, count in candidato_counts.items():
            support = count / n_total
            if support >= min_support:
                frequent_itemsets_k_plus_1.append(list(candidato))
                support_dict[candidato] = support
        
        print(f"  Se encontraron {len(frequent_itemsets_k_plus_1)} {k+1}-itemsets frecuentes")
        
    #Continua si encuentra itemsets frecuentes
        if frequent_itemsets_k_plus_1:
            all_frequent_itemsets[k+1] = frequent_itemsets_k_plus_1
            k += 1
        else:
            break
    return all_frequent_itemsets, support_dict

#Funcion para generar reglas
def generar_reglas(itemsets_frecuentes, support_dict, min_confidence=0.5):
    rules = []

    for k in range(2, len(itemsets_frecuentes) + 1):
        if k not in itemsets_frecuentes:
            continue
        for itemset in itemsets_frecuentes[k]:
            itemset_support = support_dict[tuple(itemset)]
            for i in range(len(itemset)):
                from itertools import combinations
                for antecedent_items in combinations(itemset, i):
                    antecedent = list(antecedent_items)
                    consequent = [item for item in itemset if item not in antecedent]
                    
                    # soporte antecedente
                    antecedent_support = support_dict[tuple(antecedent)]
                    
                    # Confianzita
                    confidence = itemset_support / antecedent_support
                    
                    # Si cumple con la confianza mínima, se agregar
                    if confidence >= min_confidence:
                        # lift
                        consequent_support = support_dict[tuple(consequent)]
                        lift = confidence / consequent_support
                        
                        rules.append({
                            'antecedent': antecedent,
                            'consequent': consequent,
                            'support': itemset_support,
                            'confidence': confidence,
                            'lift': lift
                        })
    
    
    if rules:
        rulesDf = pd.DataFrame(rules)

        #lift descendente
        rulesDf = rulesDf.sort_values('lift', ascending=False).reset_index(drop=True)
        return rulesDf
    else:
        return pd.DataFrame(columns=['antecedent', 'consequent', 'support', 'confidence', 'lift'])

#aplicacion en todo el algoritmo
transactions_list = sparse_transaction(order_matrix_sparse, item_mapping)

# Verificar el resultado
print(f"Número de transacciones en transactions_list: {len(transactions_list)}")
if len(transactions_list) > 0:
    print("Primeras 3 transacciones:")
    for i in range(min(3, len(transactions_list))):
        print(f"Transacción {i} (longitud {len(transactions_list[i])}): {transactions_list[i][:5]}")

#Verificacion vacias
empty_transactions = sum(1 for t in transactions_list if len(t) == 0)
print(f"Transacciones vacías: {empty_transactions} de {len(transactions_list)}")

#distribucion frecuencias items
item_freq = {}
for transaction in transactions_list:
    for item in transaction:
        item_freq[item] = item_freq.get(item, 0) + 1

#organizar por frecuencia
sorted_items = sorted(item_freq.items(), key=lambda x: x[1], reverse=True)

#y vreificamos cuantos superarin diferentes umbrales
print("Top 10 items más frecuentes:")
for item, count in sorted_items[:10]:
    support = count / len(transactions_list)
    print(f"Item: {item}, Frecuencia: {count}, Soporte: {support:.6f}")

