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

# Super Important Note on Running Ollama Models

Ollama models by default only have 2048 tokens for their context window, even for large models that could easily handle way more. This is not a large enough window to handle the Bolt.new/oTToDev prompt! You have to create a version of any model you want to use where you specify a larger context window. Luckily, it's super easy to do that.

All you have to do is:

1. Create a file called `Modelfile` (no file extension) anywhere on your computer.
2. Put in the two lines:

   ```
   FROM [Ollama model ID such as qwen2.5-coder:7b]
   PARAMETER num_ctx 32768
   ```

3. Run the command:

   ```
   ollama create -f Modelfile [your new model ID, can be whatever you want (example: qwen2.5-coder-extra-ctx:7b)]
   ```

Now you have a new Ollama model that isn't heavily limited in context length like Ollama models are by default for some reason. You'll see this new model in the list of Ollama models along with all the others you pulled!

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