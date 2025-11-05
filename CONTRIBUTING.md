# Contribuir al Sistema de Recomendaciones con Apriori

¡Gracias por tu interés en contribuir al Sistema de Recomendaciones con Apriori! Este documento proporciona pautas para contribuir a este proyecto.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [Primeros Pasos](#primeros-pasos)
- [Configuración del Entorno de Desarrollo](#configuración-del-entorno-de-desarrollo)
- [Cómo Contribuir](#cómo-contribuir)
- [Estándares de Código](#estándares-de-código)
- [Pruebas](#pruebas)
- [Proceso de Pull Request](#proceso-de-pull-request)

## 🤝 Código de Conducta

Este proyecto se adhiere a un código de conducta que todos los contribuyentes deben seguir. Por favor, sé respetuoso y constructivo en tus interacciones.

## 🚀 Primeros Pasos

1. **Haz un fork del repositorio** en GitHub
2. **Clona tu fork** localmente:
   ```bash
   git clone https://github.com/TU-USUARIO/Apriori-Latex-Project-Final.git
   cd Apriori-Latex-Project-Final
   ```

3. **Añade el repositorio upstream** como remoto:
   ```bash
   git remote add upstream https://github.com/kevarci/Apriori-Latex-Project-Final.git
   ```

## 💻 Configuración del Entorno de Desarrollo

1. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Instala las dependencias de desarrollo:**
   ```bash
   pip install black isort flake8 pytest pytest-cov
   ```

4. **Configura pre-commit hooks (opcional pero recomendado):**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## 🔧 Cómo Contribuir

### Reportar Errores

Si encuentras un error, por favor crea un issue con:
- Un título claro y descriptivo
- Pasos detallados para reproducir el error
- Comportamiento esperado vs comportamiento real
- Tu entorno (SO, versión de Python, etc.)
- Capturas de pantalla si aplica

### Sugerir Mejoras

Para solicitudes de nuevas funcionalidades:
- Usa un título claro y descriptivo
- Proporciona una descripción detallada de la funcionalidad propuesta
- Explica por qué esta funcionalidad sería útil
- Incluye ejemplos si es posible

### Contribuir con Código

1. **Crea una nueva rama** para tu funcionalidad o corrección:
   ```bash
   git checkout -b feature/nombre-de-tu-funcionalidad
   # o
   git checkout -b fix/tu-correccion-de-error
   ```

2. **Realiza tus cambios** siguiendo los estándares de código a continuación

3. **Escribe o actualiza las pruebas** para tus cambios

4. **Ejecuta las pruebas** para asegurarte de que todo pase:
   ```bash
   pytest tests/ -v
   ```

5. **Haz commit de tus cambios** con un mensaje descriptivo:
   ```bash
   git add .
   git commit -m "Agregar funcionalidad: descripción de tus cambios"
   ```

6. **Haz push a tu fork:**
   ```bash
   git push origin feature/nombre-de-tu-funcionalidad
   ```

7. **Crea un Pull Request** en GitHub

## 📝 Estándares de Código

### Guía de Estilo de Python

Seguimos la guía de estilo PEP 8 con algunas modificaciones:

- **Longitud de línea:** Máximo 100 caracteres
- **Indentación:** 4 espacios (sin tabulaciones)
- **Imports:** Organiza los imports usando `isort`
- **Formateo:** Usa `black` para formateo automático

### Formateo de Código

Formatea tu código antes de hacer commit:

```bash
# Formatear código con black
black utils/ tests/ app.py config.py

# Ordenar imports con isort
isort utils/ tests/ app.py config.py

# Verificar con flake8
flake8 utils/ tests/ app.py config.py --max-line-length=100
```

### Documentación

- Añade docstrings a todas las funciones, clases y módulos
- Usa docstrings estilo Google
- Incluye type hints cuando sea aplicable
- Actualiza README.md si añades nuevas funcionalidades

Ejemplo de docstring:

```python
def nombre_funcion(param1, param2):
    """
    Breve descripción de la función.
    
    Args:
        param1 (tipo): Descripción de param1
        param2 (tipo): Descripción de param2
        
    Returns:
        tipo: Descripción del valor de retorno
        
    Raises:
        TipoExcepcion: Descripción de cuándo se lanza esta excepción
    """
    pass
```

## 🧪 Pruebas

### Escribir Pruebas

- Escribe pruebas para todas las nuevas funcionalidades y correcciones de errores
- Coloca las pruebas en el directorio `tests/`
- Usa nombres descriptivos que expliquen qué se está probando
- Sigue el patrón Arrange-Act-Assert (Preparar-Actuar-Verificar)

Ejemplo de prueba:

```python
def test_nombre_funcion():
    """Prueba que nombre_funcion hace lo que debe hacer."""
    # Preparar (Arrange)
    datos_entrada = crear_datos_prueba()
    
    # Actuar (Act)
    resultado = nombre_funcion(datos_entrada)
    
    # Verificar (Assert)
    assert resultado == resultado_esperado
```

### Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
pytest tests/ -v

# Ejecutar pruebas con cobertura
pytest tests/ -v --cov=utils --cov-report=html

# Ejecutar archivo de prueba específico
pytest tests/test_data_loader.py -v

# Ejecutar prueba específica
pytest tests/test_data_loader.py::TestDataLoader::test_nombre_funcion -v
```

## 🔄 Proceso de Pull Request

1. **Actualiza la documentación** si es necesario
2. **Añade pruebas** para nuevas funcionalidades
3. **Asegúrate de que todas las pruebas pasen** localmente
4. **Actualiza CHANGELOG.md** con tus cambios
5. **Crea un Pull Request** con:
   - Título claro que describa los cambios
   - Descripción detallada del qué y el por qué
   - Referencia a issues relacionados (ej., "Fixes #123")
   - Capturas de pantalla para cambios en la UI

### Proceso de Revisión de PR

- Al menos un mantenedor debe revisar y aprobar
- Todas las verificaciones de CI deben pasar
- El código debe cumplir con los estándares de calidad
- La documentación debe estar actualizada

### Después de que tu PR sea Fusionado

1. **Elimina tu rama** (si usas GitHub, esto es automático)
2. **Actualiza tu repositorio local:**
   ```bash
   git checkout main
   git pull upstream main
   ```

## 📞 Obtener Ayuda

Si necesitas ayuda:
- Revisa los issues y discusiones existentes
- Haz preguntas en los comentarios de los issues
- Contacta a los mantenedores

## 🙏 ¡Gracias!

Tus contribuciones hacen que este proyecto sea mejor. ¡Gracias por tomarte el tiempo para contribuir!

---

**Mantenedores:**
- Fernanda Flores
- Kevin Arciniegas
- Giussepe Marreros

**Institución:** 4Geeks Academy
