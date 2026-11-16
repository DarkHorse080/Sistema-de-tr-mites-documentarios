
from pathlib import Path


def mostrar_tramite(datos):
    print("\n--- TRAMITE ENCONTRADO ---")
    print("Codigo:", datos[0])
    print("Resumen:", datos[1])

    if len(datos) == 22:
        print("Nombre completo:", datos[6], datos[4], datos[5])
        inicio = 10

    elif len(datos) == 20:
        print("Razon social:", datos[4])
        print("RUC:", datos[5])
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


def consultar_por_codigo(lineas):
    codigo = input("Ingrese el codigo del tramite: ").strip()

    for linea in lineas:
        if not linea.strip():
            continue

        datos = linea.strip().split(";")

        if datos[0].strip() == codigo:
            mostrar_tramite(datos)
            return

    print("No se encontro el tramite.")


def consultar_por_dni(lineas):
    dni = input("Ingrese el DNI: ").strip()

    if len(dni) != 8 or not dni.isdigit():
        print("El DNI debe tener 8 digitos.")
        return

    encontrados = 0

    for linea in lineas:
        if not linea.strip():
            continue

        datos = linea.strip().split(";")

        if len(datos) == 22 and datos[7].strip() == dni:
            mostrar_tramite(datos)
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron tramites para ese DNI.")
    else:
        print("\nTotal de tramites encontrados:", encontrados)


def consultar_por_ruc(lineas):
    ruc = input("Ingrese el RUC: ").strip()

    if len(ruc) != 11 or not ruc.isdigit():
        print("El RUC debe tener 11 digitos.")
        return

    encontrados = 0

    for linea in lineas:
        if not linea.strip():
            continue

        datos = linea.strip().split(";")

        if len(datos) == 20 and datos[3].strip().lower() == "juridica" and datos[5].strip() == ruc:
            mostrar_tramite(datos)
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron tramites para ese RUC.")
    else:
        print("\nTotal de tramites encontrados:", encontrados)


def consultar_tramite():
    carpeta = Path(__file__).resolve().parent
    ruta = carpeta / "Trámites.txt"

    if not ruta.exists():
        ruta = carpeta / "Tramites.txt"
        print("No hay tramites registrados.")
        return

    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        lineas = archivo.readlines()

    print("\n--- CONSULTA DE TRAMITES ---")
    print("1. Consultar por codigo")
    print("2. Consultar por DNI")
    print("3. Consultar por RUC")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        consultar_por_codigo(lineas)

    elif opcion == "2":
        consultar_por_dni(lineas)

    elif opcion == "3":
        consultar_por_ruc(lineas)

    else:
        print("Opcion no valida.")
