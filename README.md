# README

## Proyecto de Gestión de Repositorios en GitHub

Este proyecto es una herramienta Python que permite crear y gestionar repositorios en GitHub de manera automática. Se utiliza un modelo LLM (Large Language Model) para generar el contenido del README.md.

### Funcionalidades

- Creación de un nuevo repositorio en GitHub
- Inicialización de un nuevo repositorio local con la configuración adecuada
- Actualización de un repositorio existente con los cambios realizados

### Requisitos

- Python 3.x
- Ollama (un modelo LLM)
- Git y GitHub cuenta
- Conocimientos básicos de Git y GitHub

### Uso

1. Clonar el repositorio local.
2. Ejecutar `python main.py` para iniciar la herramienta.

### Contribuyentes

Se espera que los contribuyentes sigan las siguientes normas:

- Utilicen la estructura de directorios y archivos existente en el proyecto.
- Proporcionen un archivo `.env` con las variables de entorno necesarias.
- Verifiquen que la función `verificar_y_generar_readme` se ejecute correctamente antes de iniciar el repositorio.

### Archivos y Directorios

- `.env`: archivo de configuración con las variables de entorno necesarias.
- `gitignore_manager.py`: archivo que gestiona los archivos a ignorar en Git.
- `github_manager.py`: archivo que gestiona la creación y actualización de repositorios en GitHub.
- `main.py`: archivo principal del proyecto que llama a las funciones necesarias para inicializar o actualizar un repositorio.
- `ollama_manager.py`: archivo que utiliza el modelo LLM Ollama para generar el contenido del README.md.

### Condiciones de Uso

- La herramienta solo funciona con la versión actual del modelo LLM Ollama. No aplica la actualización automática al modelo, por lo que es necesario descargárselo y instalarlo manualmente.
- El uso de la herramienta debe ser autorizado mediante una cuenta GitHub. Los cambios en el proyecto requieren la confirmación de un administrador.