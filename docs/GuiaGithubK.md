1. Conceptos Clave
Rama principal: main (versión estable/producción).

Rama de desarrollo: Copia de main donde trabajas en nuevas features (ej: feature/nuevo-modelo).

Flujo típico:

Crear rama → Hacer cambios → Hacer pull request (PR) → Revisión → Merge a main.

2. Pasos Básicos

# A) Crear una rama nueva

git checkout main              # Parte de la rama principal
git pull                       # Actualiza tu repositorio local
git checkout -b mi-rama        # Crea y cambia a una nueva rama (ej: "eda-analysis")

### Si hay conflictos, resuelvelos en GitHub y luego en tu repositorio local.

# B) Trabajar en la rama

> Haz cambios en notebooks, scripts, o datos.

> Commits frecuentes:

git add archivo.ipynb         # Añade cambios específicos
git commit -m "EDA: análisis outliers"
git push origin mi-rama       # Sube la rama al repositorio remoto

# C) Crear un Pull Request (PR)

1. Ve a GitHub → Repositorio → "Pull Requests" → "New PR".
2. Compara mi-rama con main.
3. Describe los cambios (qué hiciste, cómo validar resultados).
4. Solicita revisión a un compañero.

# D) Mergear a main

Si el PR es aprobado:

git checkout main
git merge mi-rama
git push origin main

3. Buenas Prácticas para Data Science

> Nombres descriptivos:

    * feature/: Nuevos modelos o análisis (ej: feature/random-forest-optimization).
    * fix/: Correcciones (ej: fix/normalizacion-datos).
    * experiment/: Pruebas exploratorias (ej: experiment/llm-finetuning).

> Mantén las ramas actualizadas:

git checkout mi-rama
git merge main               # Trae cambios de main a tu rama para evitar conflictos

Usa .gitignore: Excluye archivos grandes (datasets, modelos serializados) o sensibles.

### Informacion Adicional ejemplo de un readme

Cómo Lo Documentaríamos
En el README de GitHub:

v1.0 - Algoritmo funciona PERO:  
Feature - Tarda 1 hora en datasets grandes (¡necesitamos optimizar!).  
- A veces genera reglas redundantes (ej: [A,B]→C y [B,A]→C).  
- El submuestreo no está bien implementado, ayuda pls :(

# Ejemplo de REadme para el proyecto 
Versión Actual: v1.0
Estado: 🟡 Algoritmo funcional pero con oportunidades críticas de mejora

🚀 Qué Funciona
Feature 1: Genera reglas de asociación básicas (soporte y confianza).

Feature 2: Visualización de reglas en formato JSON/CSV.

Feature 3: Soporta datasets pequeños (<10k transacciones).

⚠️ Problemas Conocidos
Rendimiento:

Tarda 1 hora+ en datasets grandes (>100k transacciones) (¡Urge optimizar con matrices sparse!).

Consumo de memoria crece exponencialmente (👀 memory_usage llega a 8GB).

Calidad de Reglas:

Genera reglas redundantes (ej: [A,B]→C y [B,A]→C se consideran distintas).

No maneja itemsets raros (precisión cae al 40% en datasets desbalanceados).

Implementación:

Submuestreo aleatorio (random_sampling()) tiene seed fijo (¡no es reproducible!).

Documentación de funciones incompleta (solo el 30% tiene docstrings 😓).