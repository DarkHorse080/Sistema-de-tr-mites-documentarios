import csv
from pathlib import Path
from operaciones import obtener_todos_los_tramites

def exportar_csv():
    try:
        carpeta = Path(__file__).resolve().parent

        # Obtener todos los trámites registrados
        tramites = obtener_todos_los_tramites()

        # Separar personas naturales y jurídicas
        personas_naturales = []
        personas_juridicas = []
        personas_naturales.append(["Código", "Resumen", "Autoridad", "Tipo de persona", "Apellido paterno", "Apellido materno", "Nombres", "Documento", "Correo", "Teléfono", "Tipo de vía", "Nombre de vía", "Tipo de zona", "Nombre de zona", "Referencia", "Departamento", "Provincia", "Distrito", "Fundamentación del pedido", "Documentos adjuntados", "Fecha", "Estado"])
        personas_juridicas.append(["Código", "Resumen", "Autoridad", "Tipo de persona", "Razón social", "Documento", "Correo", "Teléfono", "Tipo de vía", "Nombre de vía", "Tipo de zona", "Nombre de zona", "Referencia", "Departamento", "Provincia", "Distrito", "Fundamentación del pedido", "Documentos adjuntados", "Fecha", "Estado"])   
        for tramite in tramites:
            if len(tramite) == 22:
                personas_naturales.append(tramite)

            elif len(tramite) == 20:
                personas_juridicas.append(tramite)

        # Exportar personas naturales
        ruta_naturales = carpeta / "Trámites personas naturales.csv"

        with open(ruta_naturales, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(personas_naturales)

        # Exportar personas jurídicas
        ruta_juridicas = carpeta / "Trámites personas jurídicas.csv"

        with open(ruta_juridicas, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(personas_juridicas)

        print("\n¡Exportación realizada correctamente!")
        print(f"Personas naturales: {len(personas_naturales)-1}")
        print(f"Personas jurídicas: {len(personas_juridicas)-1}")
        print("Se generaron dos archivos CSV (personas naturales y jurídicas).")

    except FileNotFoundError:
        print("No se encontró el archivo Trámites.txt")

    except Exception as error:
        print(f"Error al exportar los trámites: {error}")