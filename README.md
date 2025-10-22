# 🛒 Sistema de Recomendaciones Personalizadas con Apriori y R

![Version](https://img.shields.io/badge/version-1.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

*"En este proyecto, fusionamos nuestra pasión por el Data Science con algoritmos clásicos de minería de datos para crear soluciones que transforman simples transacciones en experiencias personalizadas. Cada línea de código representa nuestro compromiso con descubrir patrones ocultos en los datos que mejoran la vida cotidiana."*

## 👥 Colaboradores

- **Fernanda Flores**
- **Kevin Arciniegas**
- **Giussepe Marreros**

**Institución:** 4Geeks Academy

---

## 📋 Descripción del Proyecto

Este proyecto implementa un **sistema de recomendaciones basado en el algoritmo Apriori** para análisis de reglas de asociación, utilizando datos de transacciones de compras de Instacart. El sistema combina la potencia de Python y R para procesar grandes volúmenes de datos, identificar patrones de compra y generar recomendaciones personalizadas.

### ✨ Características Principales

- 🛒 **Análisis de Market Basket** (Cesta de Compra) para identificar productos que se compran juntos
- ⚡ **Implementación optimizada** del algoritmo Apriori para grandes conjuntos de datos
- 🔀 **Enfoque híbrido** que combina Python para preprocesamiento y R para minería de reglas
- 📊 **Visualización interactiva** de reglas de asociación y patrones de compra
- 🎯 **Generación de recomendaciones personalizadas** basadas en comportamientos de compra
- 🌐 **Aplicación web Streamlit** para exploración interactiva de datos

---

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.7 o superior
- R 4.0 o superior (opcional, para análisis avanzado)
- Git

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/kevarci/Apriori-Latex-Project-Final.git
   cd Apriori-Latex-Project-Final
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno (opcional):**
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones personalizadas
   ```

5. **Ejecutar la aplicación Streamlit:**
   ```bash
   streamlit run app.py
   ```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📁 Estructura del Proyecto

```
Apriori-Latex-Project-Final/
├── app.py                          # Aplicación web Streamlit
├── config.py                       # Configuración del proyecto
├── requirements.txt                # Dependencias de Python
├── .env.example                    # Plantilla de configuración
├── .gitignore                      # Archivos a ignorar por Git
├── README.md                       # Este archivo
│
├── utils/                          # Módulos de utilidades
│   ├── __init__.py                # Inicialización del paquete
│   ├── data_loader.py             # Funciones de carga de datos
│   └── visualization.py           # Funciones de visualización
│
├── notebooks/                      # Jupyter notebooks
│   ├── hibridApriori.ipynb        # Notebook principal con análisis
│   └── TransactionsInstacart.csv  # Datos de transacciones
│
├── docs/                           # Documentación
│   ├── README.md                  # Documentación detallada
│   ├── GuiaGithubK.md            # Guía de GitHub
│   └── install latex.md          # Guía de instalación LaTeX
│
├── data/                           # Archivos de datos (opcional)
│   ├── TransactionsInstacart.csv
│   ├── products.csv
│   └── order_products__train.csv
│
└── main.tex                        # Presentación LaTeX del proyecto
```

---

## 🎯 Uso del Sistema

### 1. Aplicación Web Interactiva

Ejecuta la aplicación Streamlit para explorar los datos de forma interactiva:

```bash
streamlit run app.py
```

**Características de la aplicación:**
- Visualización de métricas clave
- Gráficos de productos más comprados
- Distribución de productos por orden
- Análisis estadístico detallado

### 2. Jupyter Notebooks

Abre y ejecuta el notebook principal para análisis detallado:

```bash
jupyter notebook notebooks/hibridApriori.ipynb
```

**Contenido del notebook:**
- Preprocesamiento de datos
- Implementación del algoritmo Apriori
- Generación de reglas de asociación
- Visualizaciones avanzadas
- Análisis de resultados

### 3. Usando los Módulos de Utilidades

```python
from utils.data_loader import load_and_process_data, get_product_stats
from utils.visualization import plot_key_insights

# Cargar datos
df = load_and_process_data('TransactionsInstacart.csv')

# Obtener estadísticas
stats = get_product_stats(df)
print(f"Total de órdenes: {stats['total_orders']}")

# Generar visualizaciones
fig = plot_key_insights(df)
```

---

## 🔧 Configuración

El proyecto utiliza variables de entorno para la configuración. Copia `.env.example` a `.env` y ajusta según tus necesidades:

```bash
# Parámetros del algoritmo Apriori
MIN_SUPPORT=0.01          # Soporte mínimo
MIN_CONFIDENCE=0.3        # Confianza mínima
MIN_LIFT=1.0             # Lift mínimo

# Parámetros de procesamiento de datos
MIN_PRODUCTS_PER_ORDER=2  # Mínimo de productos por orden
MAX_PRODUCTS_PER_ORDER=50 # Máximo de productos por orden

# Visualización
DEFAULT_TOP_N=20         # Número de productos top por defecto
```

---

## 📊 Metodología

El proyecto sigue un enfoque híbrido que combina Python y R:

1. **Preprocesamiento en Python:** Limpieza de datos, transformación y creación de matrices dispersas para representar transacciones.

2. **Implementación del Algoritmo Apriori:** Versión optimizada para procesar grandes volúmenes de datos mediante procesamiento por lotes.

3. **Minería de Reglas en R:** Utilización de la librería `arules` para descubrir patrones y reglas de asociación.

4. **Visualización:** Representación gráfica de las reglas descubiertas para facilitar su interpretación.

5. **Generación de Recomendaciones:** Creación de recomendaciones personalizadas basadas en las reglas de asociación descubiertas.

---

## 📈 Resultados

El sistema ha identificado patrones de compra significativos en el conjunto de datos de Instacart:

- **Soporte mínimo utilizado:** 0.01
- **Confianza mínima:** 0.3
- **Número de reglas generadas:** Más de 100 reglas significativas

Las visualizaciones generadas permiten identificar clusters de productos que se compran frecuentemente juntos, facilitando la toma de decisiones para estrategias de marketing y disposición de productos.

---

## 🛠️ Desarrollo

### Instalación de Dependencias de Desarrollo

```bash
pip install -r requirements.txt
```

### Ejecutar Tests (si están disponibles)

```bash
pytest tests/
```

### Linting y Formato de Código

```bash
# Formatear código con black
black utils/ app.py

# Linting con flake8
flake8 utils/ app.py
```

---

## 🔮 Trabajo Futuro

- [ ] Implementación de un sistema de recomendaciones en tiempo real
- [ ] Integración con plataformas de e-commerce
- [ ] Exploración de algoritmos alternativos como FP-Growth para comparar rendimiento
- [ ] Incorporación de información demográfica para recomendaciones más personalizadas
- [ ] API REST para integración con otros sistemas
- [ ] Dashboard administrativo para monitoreo de métricas
- [ ] Tests unitarios y de integración
- [ ] Documentación de API con Swagger/OpenAPI

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 📚 Referencias

- Agrawal, R., & Srikant, R. (1994). Fast algorithms for mining association rules. *Proc. 20th int. conf. very large data bases, VLDB*, 1215, 487-499.
- Hahsler, M., Grün, B., & Hornik, K. (2005). arules - A computational environment for mining association rules and frequent item sets. *Journal of Statistical Software*, 14(15), 1-25.
- Instacart Market Basket Analysis. (2017). Kaggle. https://www.kaggle.com/c/instacart-market-basket-analysis

---

## 📧 Contacto

Para preguntas o sugerencias, por favor contacta a los colaboradores:

- Fernanda Flores
- Kevin Arciniegas
- Giussepe Marreros

**Institución:** 4Geeks Academy

---

<div align="center">
  <strong>Hecho con ❤️ por el equipo de 4Geeks Academy</strong>
</div>
