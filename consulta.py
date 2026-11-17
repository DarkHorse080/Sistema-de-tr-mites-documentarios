
from pathlib import Path


# Funcion que muestra los datos de un tramite encontrado.
def mostrar_tramite(datos):
    print("\n--- TRAMITE ENCONTRADO ---")
    print("Codigo:", datos[0])
    print("Resumen:", datos[1])

    # Comprueba si el tramite pertenece a una persona natural.
    if len(datos) == 22:
        print("Nombre completo:", datos[6], datos[4], datos[5])
        inicio = 10

    # Comprueba si el tramite pertenece a una persona juridica.
    elif len(datos) == 20:
        print("Razon social:", datos[4])
        print("RUC:", datos[5])
        inicio = 8

    else:
        print("No se reconoce el formato del tramite.")
        return

    # Verifica que los datos necesarios esten completos.
    if len(datos) <= inicio + 11:
        print("Los datos del tramite estan incompletos.")
        return

    # Muestra la informacion final del tramite.
    print("Fundamentacion:", datos[inicio + 8])
    print("Documentos adjuntos:", datos[inicio + 9])
    print("Fecha:", datos[inicio + 10])
    print("Estado:", datos[inicio + 11])


# Funcion que busca un tramite utilizando su codigo.
def consultar_por_codigo(lineas):
    codigo = input("Ingrese el codigo del tramite: ").strip()

    # Recorre todos los registros del archivo.
    for linea in lineas:
        if not linea.strip():
            continue

        # Separa los datos utilizando el punto y coma.
        datos = linea.strip().split(";")

        # Compara el codigo ingresado con el codigo registrado.
        if datos[0].strip() == codigo:
            mostrar_tramite(datos)
            return

    print("No se encontro el tramite.")


# Funcion que busca tramites utilizando el DNI.
def consultar_por_dni(lineas):
    dni = input("Ingrese el DNI: ").strip()

    # Verifica que el DNI tenga exactamente 8 digitos.
    if len(dni) != 8 or not dni.isdigit():
        print("El DNI debe tener 8 digitos.")
        return

    encontrados = 0

    # Recorre los registros buscando coincidencias.
    for linea in lineas:
        if not linea.strip():
            continue

        datos = linea.strip().split(";")

        # Busca el DNI solamente en registros de personas naturales.
        if len(datos) == 22 and datos[7].strip() == dni:
            mostrar_tramite(datos)
            encontrados += 1

    # Informa si se encontraron tramites.
    if encontrados == 0:
        print("No se encontraron tramites para ese DNI.")
    else:
        print("\nTotal de tramites encontrados:", encontrados)


# Funcion que busca tramites utilizando el RUC.
def consultar_por_ruc(lineas):
    ruc = input("Ingrese el RUC: ").strip()

    # Verifica que el RUC tenga exactamente 11 digitos.
    if len(ruc) != 11 or not ruc.isdigit():
        print("El RUC debe tener 11 digitos.")
        return

    encontrados = 0

    # Recorre los registros buscando coincidencias.
    for linea in lineas:
        if not linea.strip():
            continue

        datos = linea.strip().split(";")

        # Busca el RUC solamente en registros de personas juridicas.
        if len(datos) == 20 and datos[3].strip().lower() == "juridica" and datos[5].strip() == ruc:
            mostrar_tramite(datos)
            encontrados += 1

    # Informa si se encontraron tramites.
    if encontrados == 0:
        print("No se encontraron tramites para ese RUC.")
    else:
        print("\nTotal de tramites encontrados:", encontrados)


# Funcion principal que permite seleccionar el tipo de consulta.
def consultar_tramite():

    # Obtiene la carpeta donde se encuentra este archivo Python.
    carpeta = Path(__file__).resolve().parent

    # Define la ruta del archivo donde se guardan los tramites.
    ruta = carpeta / "Trámites.txt"

    # Comprueba si existe el archivo con el nombre alternativo.
    if not ruta.exists():
        ruta = carpeta / "Tramites.txt"

    # Verifica si existe el archivo de registros.
    if not ruta.exists():
        print("No hay tramites registrados.")
        return

    # Abre el archivo y lee todos los registros.
    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        lineas = archivo.readlines()

    # Muestra las opciones disponibles para realizar una consulta.
    print("\n--- CONSULTA DE TRAMITES ---")
    print("1. Consultar por codigo")
    print("2. Consultar por DNI")
    print("3. Consultar por RUC")

    opcion = input("Seleccione una opcion: ").strip()

    # Ejecuta la funcion segun la opcion seleccionada.
    if opcion == "1":
        consultar_por_codigo(lineas)

    elif opcion == "2":
        consultar_por_dni(lineas)

    elif opcion == "3":
        consultar_por_ruc(lineas)

    else:
        print("Opcion no valida.")
