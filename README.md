readme_contenido")
        readme_file:
            archivo_readme.write(readme_contenido)
        print("README.md generado exitosamente.")
        return True

    except Exception as e:
        print(f"Error al generar el README.md: {e}")
        return False
```