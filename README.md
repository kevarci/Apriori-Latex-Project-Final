# Proyecto de Análisis de Reglas de Asociación con Apriori

## Configuración del Entorno

Para configurar el entorno de desarrollo:

1. Crear un entorno virtual:
-python -m venv venv

2. Activar el entorno virtual:
- Windows (cmd): `venv\Scripts\activate`
- Windows (PowerShell): `venv\Scripts\Activate.ps1`
- Linux/Mac: `source venv/bin/activate`

3. Instalar dependencias:
- pip install -r requirements.txt

## Implementaciones Recientes

### Preprocesamiento de Datos
- Carga de datos de transacciones desde el archivo 'order_products__train.csv'
- Implementación de enfoque optimizado para manejar grandes volúmenes de datos:
- Selección de los 1000 productos más frecuentes para reducir dimensionalidad
- Creación de matriz binaria usando crosstab para representar presencia/ausencia de productos
- Conversión a formato binario (1 para presencia, 0 para ausencia)

### Estructuras de Datos Eficientes
- Implementación de múltiples estructuras para almacenar transacciones:
- Estructura de diccionario: Eficiente para búsquedas y operaciones de conjuntos
- Arrays de bits: Representación compacta en memoria para operaciones bit a bit
- DataFrame sparse: Combinación de pandas con ahorro de memoria para matrices dispersas
- Cada estructura optimizada para diferentes fases del algoritmo Apriori

### Generación de Itemsets Frecuentes
- Implementación de la generación de 1-itemsets frecuentes
- Establecimiento de umbral de soporte mínimo configurable
- Cálculo del soporte para cada producto individual
- Filtrado de productos que cumplen con el soporte mínimo
- Ordenamiento de itemsets por soporte en orden descendente
- Preparación de estructura de datos para generación de itemsets de mayor tamaño

### Generación de Itemsets de Mayor Tamaño
- Implementación completa de la generación de k-itemsets (k ≥ 2)
- Algoritmo de poda basado en la propiedad de anti-monotonía del soporte
- Optimización de memoria mediante técnicas de hash para candidatos
- Paralelización del proceso de conteo para mejorar rendimiento en datasets grandes

### Generación de Reglas de Asociación
- Implementación del algoritmo para extraer reglas a partir de itemsets frecuentes
- Cálculo de métricas de interés: soporte, confianza, lift y conviction
- Filtrado de reglas según umbrales configurables de confianza mínima
- Ordenamiento de reglas por relevancia según múltiples criterios

### Integración con LaTeX
- Generación automática de documentos LaTeX con resultados del análisis
- Creación de tablas formateadas con las reglas más relevantes
- Inclusión de gráficos de visualización de métricas
- Exportación a PDF mediante integración con compilador LaTeX

### Interfaz de Usuario
- Desarrollo de interfaz gráfica para configuración de parámetros
- Visualización interactiva de resultados y métricas
- Opciones de filtrado y ordenamiento de reglas en tiempo real
- Exportación de resultados en múltiples formatos (CSV, Excel, PDF)

### Últimas Optimizaciones del Algoritmo Apriori
- Mejora significativa en la generación de candidatos para reducir uso de memoria
- Implementación de cálculo de soporte optimizado mediante operaciones de conjuntos
- Incorporación de procesamiento por lotes para manejar grandes volúmenes de datos
- Precomputación de conjuntos de transacciones para acelerar verificación de candidatos
- Filtrado inteligente de transacciones por longitud mínima para evitar procesamiento innecesario
- Adición de indicadores de progreso durante el procesamiento de grandes conjuntos de datos
- Optimización de la fase de conteo mediante el uso eficiente de operaciones de subconjuntos
- Mejora en la gestión de memoria para permitir umbrales de soporte más bajos

### Próximos Pasos
- Implementación de algoritmos de visualización avanzada de reglas
- Integración con técnicas de clustering para agrupamiento de reglas similares
- Desarrollo de módulo de interpretación automática de reglas
- Optimización adicional para conjuntos de datos ultra grandes