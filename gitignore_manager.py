import os

# Contenido genérico para .gitignore
GITIGNORE_CONTENT = """
# Entornos virtuales y dependencias
venv/
.env/
node_modules/
*.lock
yarn-error.log
package-lock.json

# Archivos temporales y compilados
*.pyc
*.pyo
*.pyd
*.class
*.o
*.obj
*.so
*.dll
*.exe
__pycache__/
*.log
*.tmp
*.swp

# Archivos del sistema operativo
.DS_Store
Thumbs.db
desktop.ini

# Configuración de IDEs
.vscode/
.idea/
*.iml
*.suo
*.ntvs*
*.njsproj
*.sln

# Archivos de Git
.git/
*.orig
*.rej

# Archivos de compilación y despliegue
dist/
build/
out/
target/
coverage/
*.coverage
.jest/
.cache/
*.war
*.jar
*.apk
*.ipa

# Archivos de bases de datos y configuraciones sensibles
*.sqlite3
*.db
*.sql

# Archivos que suelen contener variables de entorno
.env
.env.*       # Archivos adicionales como .env.production, .env.local
*.env
*.env.*      # Variaciones del estándar .env.*
secrets.json
keys.json
config.json
config.yaml
*.secret
*.key
*.pem
*.crt
*.p12
*.cer

# Configuración de Docker y Kubernetes
docker-compose.override.yml
*.dockerignore
*.kubeconfig
*.helmrelease
""".strip()

def crear_gitignore(ruta_proyecto):
    """
    Crea un archivo .gitignore en la raíz del proyecto si no existe.
    """
    ruta_gitignore = os.path.join(ruta_proyecto, ".gitignore")

    if os.path.exists(ruta_gitignore):
        print(".gitignore ya existe. No se realizaron cambios.")
        return

    try:
        with open(ruta_gitignore, "w", encoding="utf-8") as archivo_gitignore:
            archivo_gitignore.write(GITIGNORE_CONTENT)
        print(".gitignore creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo .gitignore: {e}")
