# 🚀 Apriori Hybrid Engine: Sistema de Minería Senior

![Version](https://img.shields.io/badge/version-1.1-blue.svg)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![R-arules](https://img.shields.io/badge/Engine-R--arules-276DC3.svg)](https://cran.r-project.org/web/packages/arules/index.html)

## 👤 Colaboradores
- **Fernanda Flores**
- **Kevin Arciniegas**
- **Giussepe Marreros**

## 📝 Descripción
Este proyecto implementa un motor de minería de reglas de asociación de alto rendimiento para el dataset de Instacart (131k+ transacciones). Utiliza un enfoque híbrido que combina una implementación optimizada en Python con el poder del paquete `arules` de R, permitiendo transformar simples transacciones en experiencias personalizadas.

## 📁 Estructura del Proyecto (Arquitectura Senior)

```text
├── data/
│   ├── raw/                # Datasets originales (Inmutables)
│   ├── processed/          # Datos transformados (Cestas de compra)
│   └── results/            # Reglas generadas y métricas
├── core/                   # Lógica central del algoritmo (Motor Híbrido)
├── utils/                  # Procesamiento de datos
├── notebooks/              # Experimentación inicial (Legacy)
├── docs/                   # Documentación técnica y reportes (LaTeX)
├── main.py                 # Interfaz de Línea de Comandos (CLI)
└── requirements.txt        # Dependencias del proyecto
```

## ✨ Características Principales

*   **Motor Dual Inteligente**: Fallback automático a un motor Python (Batch-Optimized) si R no está disponible.
*   **Minería por Lotes**: Capacidad para procesar cientos de miles de transacciones sin desbordar la memoria RAM.
*   **Resultados de Alto Desempeño**: Generación eficiente de métricas de Soporte, Confianza y Lift.

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/apriori-hybrid-engine.git
cd apriori-hybrid-engine
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar CLI
```bash
python main.py
```

## 🧠 Metodología

El proyecto separa la **fase de experimentación** (ubicada en `notebooks/`) de la **fase de producción** (ubicada en `core/`). El algoritmo Apriori implementado utiliza un índice por prefijo y poda proactiva para reducir el espacio de búsqueda de candidatos, permitiendo ejecuciones eficientes incluso en hardware doméstico.

---
**Desarrollado por Antigravity AI** | *Arquitectura de Datos Senior para Portafolio de Alto Impacto.*
