import os
from gitignore_manager import crear_gitignore
from github_manager import crear_repositorio, inicializar_git, actualizar_repositorio
from ollama_manager import generar_readme_con_ollama  # Asegúrate de importar la función de generación de README

def verificar_y_generar_readme(ruta_proyecto):
    """
    Verifica si existe un README.md en el proyecto y pregunta si se debe reemplazar.
    Si no existe, lo genera automáticamente.
    """
    ruta_readme = os.path.join(ruta_proyecto, "README.md")
    
    if os.path.exists(ruta_readme):
        respuesta = input("El archivo README.md ya existe. ¿Deseas reemplazarlo? [s/n]: ").strip().lower()
        if respuesta != "s":
            print("No se reemplazará el README.md existente.")
            return False
    # Generar el README.md con ollama
    return generar_readme_con_ollama(ruta_proyecto)

if __name__ == "__main__":
    opcion = input("¿Es un repositorio nuevo (n) o un commit en uno existente (e)? [n/e]: ").strip().lower()
    ruta_proyecto = input("Ingrese la ruta de la carpeta del proyecto: ").strip()

    if not os.path.exists(ruta_proyecto):
        print("La carpeta especificada no existe. Por favor, verifica la ruta.")
        exit()

    if opcion == "n":
        nombre_repositorio = input("Ingrese el nombre del nuevo repositorio: ").strip()
        repo_url = crear_repositorio(nombre_repositorio)
        if repo_url:
            # Crear o verificar README.md antes de inicializar el repositorio
            if verificar_y_generar_readme(ruta_proyecto):
                inicializar_git(ruta_proyecto, repo_url)
    elif opcion == "e":
        if verificar_y_generar_readme(ruta_proyecto):
            actualizar_repositorio(ruta_proyecto)
    else:
        print("Opción no válida. Por favor, seleccione 'n' para nuevo o 'e' para existente.")