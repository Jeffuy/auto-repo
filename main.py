import os
from gitignore_manager import crear_gitignore
from github_manager import crear_repositorio, inicializar_git, actualizar_repositorio

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
            inicializar_git(ruta_proyecto, repo_url)
    elif opcion == "e":
        actualizar_repositorio(ruta_proyecto)
    else:
        print("Opción no válida. Por favor, seleccione 'n' para nuevo o 'e' para existente.")