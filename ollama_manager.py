import subprocess
import os

OLLAMA_MODEL = "llama3.2"
MAX_FILE_CONTENT_LENGTH = 5000
README_PROMPT_TEMPLATE = """
You are a technical documentation assistant. Generate a professional and structured README.md file for the following project.
Make sure to include:
- **Project Purpose**: What the project is and why it is useful.
- **Installation Instructions**: How to set up the project.
- **Usage**: Examples of how to use it.
- **Contributing**: How contributors can help.
- **License**: If applicable.

Keep the tone professional and concise. Avoid introducing yourself or adding unnecessary comments. 

Project files:
{archivos}

Also, copy me the prompt you received
"""

# Carpetas y archivos a ignorar
IGNORAR_CARPETAS = [
    "venv", "__pycache__", ".git", "node_modules", ".idea", ".vscode", "dist", "build",
    "coverage", ".pytest_cache", ".mypy_cache", ".cache"
]
IGNORAR_ARCHIVOS = [
    ".DS_Store", "Thumbs.db", "desktop.ini", "*.log", "*.tmp", "*.lock", "*.swp",
    "*.class", "*.o", "*.obj", "*.so", "*.dll", "*.exe", "*.pyc", "*.pyo",
    "*.pyd", "*.db", "*.sqlite3", "*.env"
]

def debe_ignorar(ruta):
    """
    Verifica si una carpeta o archivo debe ser ignorado según las listas de exclusión.
    """
    nombre = os.path.basename(ruta)

    # Verificar carpetas ignoradas
    if os.path.isdir(ruta):
        return nombre in IGNORAR_CARPETAS

    # Verificar archivos ignorados
    for patron in IGNORAR_ARCHIVOS:
        if nombre.endswith(patron) or nombre == patron:
            return True
    return False

def listar_archivos_y_contenido(ruta):
    """
    Lee todos los archivos en el directorio y concatena su contenido,
    ignorando carpetas y archivos irrelevantes.
    """
    archivos_contenido = []
    for raiz, carpetas, archivos in os.walk(ruta):
        # Filtrar carpetas a ignorar
        carpetas[:] = [c for c in carpetas if not debe_ignorar(os.path.join(raiz, c))]

        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            if debe_ignorar(ruta_completa):
                continue
            try:
                with open(ruta_completa, "r", encoding="utf-8", errors="replace") as f:
                    contenido = f.read()[:MAX_FILE_CONTENT_LENGTH]
                    archivos_contenido.append(f"Archivo: {archivo}\n{contenido}\n")
            except Exception as e:
                print(f"Error al leer el archivo {ruta_completa}: {e}")
    return "\n".join(archivos_contenido)

def generar_readme_con_ollama(ruta_proyecto):
    """
    Genera un README.md usando un modelo LLM.
    """
    try:
        archivos_contenido = listar_archivos_y_contenido(ruta_proyecto)
        if not archivos_contenido:
            print("No se encontraron archivos para incluir en el README.md.")
            return False

        prompt = README_PROMPT_TEMPLATE.format(archivos=archivos_contenido)
        comando = ["ollama", "run", OLLAMA_MODEL, prompt]
        resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
        )

        if resultado.returncode != 0:
            print("Error al comunicarse con OLLAMA:", resultado.stderr)
            return False

        readme_contenido = resultado.stdout.strip()
        with open(os.path.join(ruta_proyecto, "README.md"), "w", encoding="utf-8") as archivo_readme:
            archivo_readme.write(readme_contenido)
        print("README.md generado exitosamente.")
        return True
    except Exception as e:
        print("Error al generar el README.md:", e)
        return False