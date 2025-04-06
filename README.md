# Sistema de Recomendaciones Personalizadas con Apriori y R

![Version](https://img.shields.io/badge/version-1.1-blue.svg)

*"En este proyecto, fusionamos nuestra pasión por el Data Science con algoritmos clásicos de minería de datos para crear soluciones que transforman simples transacciones en experiencias personalizadas. Cada línea de código representa nuestro compromiso con descubrir patrones ocultos en los datos que mejoran la vida cotidiana."*

## Colaboradores
- Fernanda Flores
- Kevin Arciniegas
- Giussepe Marreros

## Descripción del Proyecto

Este proyecto implementa un sistema de recomendaciones basado en el algoritmo Apriori para análisis de reglas de asociación, utilizando datos de transacciones de compras de Instacart. El sistema combina la potencia de Python y R para procesar grandes volúmenes de datos, identificar patrones de compra y generar recomendaciones personalizadas.

## Características Principales

- Análisis de Market Basket (Cesta de Compra) para identificar productos que se compran juntos
- Implementación optimizada del algoritmo Apriori para grandes conjuntos de datos
- Enfoque híbrido que combina Python para preprocesamiento y R para minería de reglas
- Visualización interactiva de reglas de asociación y patrones de compra
- Generación de recomendaciones personalizadas basadas en comportamientos de compra

## Configuración del Entorno

### Requisitos Previos
- Python 3.7+
- R 4.0+
- Jupyter Notebook

### Instalación

1. Crear un entorno virtual:
python -m venv venv
2. Activar el entorno virtual:
### Windows
venv\Scripts\activate
### macOS/Linux
source venv/bin/activate
3. Instalar las dependencias de python:
pip install pandas numpy matplotlib plotly networkx scipy mlxtend
4. Instalar las dependencias de R:
install.packages(c("arules", "arulesViz", "tidyverse", "readr"))

## Estructura del Proyecto
├── data/
│   ├── order_products__train.csv
│   └── products.csv
├── notebooks/
│   ├── hibridApriori.ipynb
│   └── visualizacion_reglas.ipynb
├── docs/
│   └── Sistema de Recomendaciones personalizadas con Apriori.pdf
└── README.md

## Metodología
El proyecto sigue un enfoque híbrido que combina Python y R para el análisis de reglas de asociación:

1. Preprocesamiento en Python : Limpieza de datos, transformación y creación de matrices dispersas para representar transacciones.
2. Implementación del Algoritmo Apriori : Versión optimizada para procesar grandes volúmenes de datos mediante procesamiento por lotes.
3. Minería de Reglas en R : Utilización de la librería arules para descubrir patrones y reglas de asociación.
4. Visualización : Representación gráfica de las reglas descubiertas para facilitar su interpretación.
5. Generación de Recomendaciones : Creación de recomendaciones personalizadas basadas en las reglas de asociación descubiertas.

## Resultados
El sistema ha identificado patrones de compra significativos en el conjunto de datos de Instacart, con reglas de asociación que muestran relaciones interesantes entre productos. Algunas de las métricas clave incluyen:

- Soporte mínimo utilizado: 0.01
- Confianza mínima: 0.3
- Número de reglas generadas: Más de 100 reglas significativas
Las visualizaciones generadas permiten identificar clusters de productos que se compran frecuentemente juntos, facilitando la toma de decisiones para estrategias de marketing y disposición de productos.

## Uso del Sistema
### Ejecución del Análisis
1. Abrir el notebook hibridApriori.ipynb en Jupyter Notebook:
jupyter notebook notebooks/hibridApriori.ipynb
2. Ejecutar las celdas de código en secuencia para cargar los datos, preprocesarlos, ejecutar el algoritmo Apriori y generar recomendaciones.
3. Visualizar las reglas de asociación generadas y las recomendaciones personalizadas.
jupyter notebook notebooks/visualizacion_reglas.ipynb

### Generación de Recomendaciones
El sistema puede generar recomendaciones de dos formas:

1. Recomendaciones basadas en productos : Dado un producto, recomienda otros productos que se compran frecuentemente junto con él.
2. Recomendaciones basadas en carrito : Analiza los productos en el carrito actual y sugiere productos adicionales basados en patrones de compra.

## Conclusiones
El enfoque híbrido Python-R ha demostrado ser efectivo para el análisis de grandes volúmenes de datos de transacciones. Las optimizaciones implementadas en el algoritmo Apriori permiten procesar eficientemente conjuntos de datos que de otra manera serían computacionalmente prohibitivos.

Las reglas de asociación descubiertas proporcionan insights valiosos sobre el comportamiento de compra de los clientes, permitiendo personalizar recomendaciones y mejorar la experiencia de usuario en plataformas de comercio electrónico.

## Trabajo Futuro
- Implementación de un sistema de recomendaciones en tiempo real
- Integración con plataformas de e-commerce
- Exploración de algoritmos alternativos como FP-Growth para comparar rendimiento
- Incorporación de información demográfica para recomendaciones más personalizadas

## Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## Referencias
- Agrawal, R., & Srikant, R. (1994). Fast algorithms for mining association rules. Proc. 20th int. conf. very large data bases, VLDB, 1215, 487-499.
- Hahsler, M., Grün, B., & Hornik, K. (2005). arules - A computational environment for mining association rules and frequent item sets. Journal of Statistical Software, 14(15), 1-25.
- Instacart Market Basket Analysis. (2017). Kaggle. https://www.kaggle.com/c/instacart-market-basket-analysis