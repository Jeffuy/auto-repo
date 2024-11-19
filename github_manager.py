import os
import subprocess
import requests
from dotenv import load_dotenv
from ollama_manager import generar_readme_con_ollama
from gitignore_manager import crear_gitignore

# Cargar variables desde el archivo .env
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Carga el token desde la variable de entorno
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")  # Carga el usuario desde la variable de entorno
DEFAULT_BRANCH = "main"

def crear_repositorio(nombre_repositorio):
    """
    Crea un repositorio en GitHub usando la API.
    """
    if not GITHUB_TOKEN:
        print("No se encontró un token configurado. Por favor, verifica la variable GITHUB_TOKEN.")
        return None

    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"name": nombre_repositorio, "private": False}
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Repositorio '{nombre_repositorio}' creado con éxito.")
        return f"https://github.com/{GITHUB_USERNAME}/{nombre_repositorio}.git"
    else:
        print("Error al crear el repositorio:", response.json())
        return None

def inicializar_git(ruta_proyecto, repo_url):
    """
    Inicializa un nuevo repositorio local y lo sube a GitHub.
    """
    try:
        os.chdir(ruta_proyecto)
        crear_gitignore(ruta_proyecto)

        if not generar_readme_con_ollama(ruta_proyecto):
            print("No se pudo generar el README.md. Abortando el proceso.")
            return

        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
        subprocess.run(["git", "branch", "-M", DEFAULT_BRANCH], check=True)
        subprocess.run(["git", "push", "-u", "origin", DEFAULT_BRANCH], check=True)
        print(f"Repositorio subido con éxito a {repo_url}")
    except Exception as e:
        print("Error al inicializar el repositorio:", e)
    finally:
        os.chdir("..")

def actualizar_repositorio(ruta_proyecto):
    """
    Añade, commitea y empuja los cambios a un repositorio existente.
    """
    try:
        os.chdir(ruta_proyecto)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Update"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Cambios subidos exitosamente.")
    except Exception as e:
        print("Error al actualizar el repositorio:", e)
    finally:
        os.chdir("..")