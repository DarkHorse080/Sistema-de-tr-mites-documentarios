
from pathlib import Path


def consultar_tramite():
    print("\n--- CONSULTA DE TRAMITES ---")
    codigo = input("Ingrese el codigo del tramite: ").strip()

    carpeta = Path(__file__).resolve().parent
    ruta = carpeta / "Trámites.txt"

    if not ruta.exists():
        ruta = carpeta / "Tramites.txt"

    if not ruta.exists():
        print("No hay tramites registrados.")
        return

    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        if not linea.strip():
            continue

        datos = linea.strip().split(";")

        if datos[0].strip() == codigo:
            print("\n--- TRAMITE ENCONTRADO ---")
            print("Codigo:", datos[0])
            print("Resumen:", datos[1])

            if len(datos) == 22:
                print("Nombre completo:", datos[6], datos[4], datos[5])
                inicio = 10

            elif len(datos) == 20:
                print("Razon social:", datos[4])
                inicio = 8

            else:
                print("No se reconoce el formato del tramite.")
                return

            if len(datos) <= inicio + 11:
                print("Los datos del tramite estan incompletos.")
                return

            print("Fundamentacion:", datos[inicio + 8])
            print("Documentos adjuntos:", datos[inicio + 9])
            print("Fecha:", datos[inicio + 10])
            print("Estado:", datos[inicio + 11])
            return

    print("No se encontro el tramite.")
