# Proyecto Final en LaTeX: Configuración en VS Code y Codespaces

Este documento guía a los colaboradores en la configuración y uso de Visual Studio Code (VS Code) para quienes trabajen localmente, y GitHub Codespaces para quienes trabajen en la nube. Ambos entornos están diseñados para colaborar sin problemas en el mismo proyecto.

---

## **Requisitos Previos**

1. **Para trabajar en VS Code:**

   - Tener instalados:
     - [Visual Studio Code](https://code.visualstudio.com/).
     - Una distribución de LaTeX:
       - **Windows:** [MiKTeX](https://miktex.org/).
       - **macOS:** [MacTeX](http://www.tug.org/mactex/).
       - **Linux:** TeX Live (`sudo apt-get install texlive-full`).
     - [Git](https://git-scm.com/).

2. **Para trabajar en Codespaces:**
   - Tener una cuenta en GitHub.
   - Acceso al repositorio del proyecto.
   - Habilitar GitHub Codespaces en tu cuenta. Esto no requiere instalación local de herramientas.

---

## **Configuración del Proyecto en VS Code (Local)**

1. **Instalar Extensión "LaTeX Workshop":**

   - Abre VS Code y ve al ícono de extensiones (barra lateral izquierda).
   - Busca `LaTeX Workshop` y haz clic en "Install".

2. **Configurar un Proyecto Local:**

   - Crea una carpeta para tu proyecto, por ejemplo: `Proyecto_Final_LaTeX`.
   - Abre la carpeta en VS Code (**File > Open Folder...**).
   - Crea un archivo `main.tex` y escribe o copia tu código LaTeX.

3. **Compilar un Archivo LaTeX:**

   - Abre `main.tex` en VS Code.
   - Ingresar en terminal `pdflatex main.tex` para compilar. Esto generará un archivo `main.pdf`.

4. **Subir Cambios a GitHub:**
   - Usa Git desde la terminal de VS Code para sincronizar tus cambios con el repositorio. Por ejemplo:
     ```bash
     git add .
     git commit -m "Descripción de los cambios"
     git push
     ```

---

## **Configuración del Proyecto en Codespaces (Nube)**

1. **Crear un Codespace:**

   - Ve al repositorio en GitHub y haz clic en la pestaña **Codespaces**.
   - Haz clic en "Create Codespace on Main" para iniciar un entorno en la nube.

2. **Entorno Preconfigurado:**

   - Si el repositorio contiene un archivo `.devcontainer/devcontainer.json`, el Codespace cargará automáticamente LaTeX y todas las herramientas necesarias.
   - Si no existe, el entorno se configurará de forma básica.

3. **Compilar un Archivo LaTeX:**

   - Abre el archivo `main.tex` en Codespaces.
   - Usa el comando `Ctrl+Alt+B` para compilar y generar `main.pdf`.

4. **Sincronizar Cambios:**
   - Al guardar tus cambios, usa Git para subirlos al repositorio:
     ```bash
     git add .
     git commit -m "Descripción de los cambios"
     git push
     ```

---

## **Colaboración entre VS Code y Codespaces**

### Sincronizar Cambios

1. **Desde Codespaces o VS Code:** Usa `git pull` antes de comenzar a trabajar, para asegurarte de tener los cambios más recientes:
   ```bash
   git pull origin main
   ```
