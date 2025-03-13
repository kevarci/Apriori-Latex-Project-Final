# Proyecto de Análisis de Reglas de Asociación con Apriori

## Implementaciones Recientes

### Preprocesamiento de Datos
- Carga de datos de transacciones desde el archivo 'order_products__train.csv'
- Implementación de enfoque optimizado para manejar grandes volúmenes de datos:
  - Selección de los 1000 productos más frecuentes para reducir dimensionalidad
  - Creación de matriz binaria usando crosstab para representar presencia/ausencia de productos
  - Conversión a formato binario (1 para presencia, 0 para ausencia)

### Generación de Itemsets Frecuentes
- Implementación de la generación de 1-itemsets frecuentes
- Establecimiento de umbral de soporte mínimo configurable
- Cálculo del soporte para cada producto individual
- Filtrado de productos que cumplen con el soporte mínimo
- Ordenamiento de itemsets por soporte en orden descendente
- Preparación de estructura de datos para generación de itemsets de mayor tamaño

### Próximos Pasos
- Generación de itemsets de mayor tamaño (2-itemsets, 3-itemsets, etc.)
- Implementación de reglas de asociación basadas en los itemsets frecuentes
- Evaluación de reglas mediante métricas como soporte, confianza y lift
- Visualización de resultados y patrones descubiertos