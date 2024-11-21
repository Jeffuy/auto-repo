# Proyecto de Gestión de Repositorios
## Descripción

Este proyecto es una herramienta de gestión de repositorios en GitHub, diseñada para ayudar a los desarrolladores a crear, mantener y compartir proyectos de manera eficiente. La herramienta utiliza la API de GitHub y el modelo LLM OLLAMA para generar un archivo README con ayuda del usuario.

## Uso

1. Seleccionar el tipo de repositorio deseado (nuevo o existente).
2. Introducir la ruta del proyecto.
3. Seleccionar la opción de crear un nuevo repositorio o subir cambios a un repositorio existente.
4. La herramienta generará un archivo README con ayuda del usuario utilizando el modelo LLM OLLAMA.

## Funcionalidades

* Creación de nuevos repositorios en GitHub
* Subida de cambios a repositorios existentes
* Generación de archivos README con ayuda del usuario
* Utilización de la API de GitHub para interactuar con los repositorios

## Arquitectura

La herramienta se compone de varios módulos, cada uno con su propia responsabilidad:

* `gitignore_manager.py`: Gestiona el archivo `.gitignore` y ignora carpetas y archivos irrelevantes.
* `github_manager.py`: Interactúa con la API de GitHub para crear y subir repositorios.
* `ollama_manager.py`: Genera un archivo README con ayuda del usuario utilizando el modelo LLM OLLAMA.

## Requisitos

* Python 3.x
* Git
* OLLAMA instalado en el sistema operativo

## Contribuyentes

Este proyecto está abierto a contribuciones. Si deseas ayudar, por favor envíase una solicitud de colaboración al correo electrónico asociado con la variable `GITHUB_USERNAME` en el archivo `.env`.

# Contribuir
Para contribuir al proyecto, sigue los siguientes pasos:

1. Clona el repositorio localmente.
2. Crea una nueva rama para tu trabajo: `git branch nombre-rama`
3. Realiza tus cambios y actualiza la rama principal: `git pull --rebase origin nombre-rama`
4. Compite tus cambios: `git commit -m "Mensaje del commit"`
5. Crea un nuevo Merge Request en GitHub.
6. Espera a que se aprueben tus cambios.

# Arquitectura de Docker
El proyecto utiliza Docker para crear una imagen ligera y eficiente.

* La imagen de base es `python:3.9-slim`
* Se agregan los siguientes paquetes:
 + `gitignore-manager`
 + `github-manager`
 + `ollama-manager`

# Configuración de Kubernetes
La herramienta se puede desplegar en un clúster de Kubernetes utilizando la API de Docker.

* La configuración de deployment utiliza el formato YAML.
* Se define un servicio de tipo LoadBalancer para acceder al proyecto desde fuera del clúster.