
from pathlib import Path


# Funcion que muestra los datos completos de un tramite encontrado.
def mostrar_tramite(datos):

    # Muestra los datos principales del tramite.
    print("\n--- TRAMITE ENCONTRADO ---")
    print("Codigo:", datos[0])
    print("Resumen:", datos[1])

    # Comprueba si el tramite pertenece a una persona natural o juridica.
    if len(datos) == 22:
        # Muestra el nombre completo de la persona natural.
        print("Nombre completo:", datos[6], datos[4], datos[5])
        inicio = 10

    elif len(datos) == 20:
        # Muestra la razon social y el RUC de la empresa.
        print("Razon social:", datos[4])
        print("RUC:", datos[5])
        inicio = 8

    else:
        # Informa si el formato del registro no es reconocido.
        print("No se reconoce el formato del tramite.")
        return

    # Comprueba que el registro tenga todos los datos necesarios.
    if len(datos) <= inicio + 11:
        print("Los datos del tramite estan incompletos.")
        return

    # Muestra la informacion final del tramite.
    print("Fundamentacion:", datos[inicio + 8])
    print("Documentos adjuntos:", datos[inicio + 9])
    print("Fecha:", datos[inicio + 10])
    print("Estado:", datos[inicio + 11])


# Funcion que permite buscar un tramite mediante su codigo.
def consultar_por_codigo(lineas):

    # Solicita el codigo que se desea buscar.
    codigo = input("Ingrese el codigo del tramite: ").strip()

    # Recorre todos los registros almacenados en el archivo.
    for linea in lineas:

        # Omite las lineas que se encuentran vacias.
        if not linea.strip():
            continue

        # Separa los datos del registro utilizando el punto y coma.
        datos = linea.strip().split(";")

        # Compara el codigo ingresado con el codigo almacenado.
        if datos[0].strip() == codigo:
            mostrar_tramite(datos)
            return

    # Informa si no se encontro ningun tramite con ese codigo.
    print("No se encontro el tramite.")


# Funcion que permite buscar todos los tramites mediante el DNI.
def consultar_por_dni(lineas):

    # Solicita el DNI al usuario.
    dni = input("Ingrese el DNI: ").strip()

    # Comprueba que el DNI tenga exactamente 8 digitos numericos.
    if len(dni) != 8 or not dni.isdigit():
        print("El DNI debe tener 8 digitos.")
        return

    # Inicializa el contador de tramites encontrados.
    encontrados = 0

    # Recorre todos los registros del archivo.
    for linea in lineas:

        # Omite los registros vacios.
        if not linea.strip():
            continue

        # Separa los campos del registro en una lista.
        datos = linea.strip().split(";")

        # Comprueba que sea una persona natural y que el DNI coincida.
        if len(datos) == 22 and datos[7].strip() == dni:

            # Muestra los datos del tramite encontrado.
            mostrar_tramite(datos)

            # Aumenta el contador de resultados.
            encontrados += 1

    # Muestra un mensaje dependiendo de los resultados obtenidos.
    if encontrados == 0:
        print("No se encontraron tramites para ese DNI.")
    else:
        print("\nTotal de tramites encontrados:", encontrados)


# Funcion que permite buscar todos los tramites mediante el RUC.
def consultar_por_ruc(lineas):

    # Solicita el RUC al usuario.
    ruc = input("Ingrese el RUC: ").strip()

    # Comprueba que el RUC tenga exactamente 11 digitos numericos.
    if len(ruc) != 11 or not ruc.isdigit():
        print("El RUC debe tener 11 digitos.")
        return

    # Inicializa el contador de tramites encontrados.
    encontrados = 0

    # Recorre todos los registros almacenados.
    for linea in lineas:

        # Omite las lineas vacias del archivo.
        if not linea.strip():
            continue

        # Separa los datos del registro utilizando el punto y coma.
        datos = linea.strip().split(";")

        # Comprueba que sea una persona juridica y que el RUC coincida.
        if len(datos) == 20 and datos[3].strip().lower() == "juridica" and datos[5].strip() == ruc:

            # Muestra la informacion del tramite encontrado.
            mostrar_tramite(datos)

            # Aumenta el contador de resultados.
            encontrados += 1

    # Informa si se encontraron tramites relacionados con el RUC.
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

    # Comprueba si el archivo existe con el nombre alternativo.
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

    # Solicita al usuario que seleccione una opcion.
    opcion = input("Seleccione una opcion: ").strip()

    # Ejecuta la funcion correspondiente a la opcion seleccionada.
    if opcion == "1":
        consultar_por_codigo(lineas)

    elif opcion == "2":
        consultar_por_dni(lineas)

    elif opcion == "3":
        consultar_por_ruc(lineas)

    else:
        # Informa cuando el usuario ingresa una opcion incorrecta.
        print("Opcion no valida.")
