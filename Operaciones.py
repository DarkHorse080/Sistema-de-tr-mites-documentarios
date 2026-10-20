
from pathlib import Path


def convertir_a_texto(lista):
    return ";".join(lista)


def convertir_a_lista(texto):
    return texto.split(";")


def obtener_todos_los_tramites():
    ruta = Path("Trámites.txt")

    if not ruta.exists():
        return []

    tramites = open(ruta, "r", encoding="utf-8-sig")
    lineas = tramites.readlines()
    tramites.close()

    lista_tramites = []

    for linea in lineas:
        linea_limpia = linea.strip()

        if linea_limpia != "":
            datos = convertir_a_lista(linea_limpia)
            lista_tramites.append(datos)

    return lista_tramites


def mostrar_todos_los_tramites():
    tramites = obtener_todos_los_tramites()

    if len(tramites) == 0:
        print("\nNo hay trámites registrados en el sistema.")
    else:
        print("\n" + "=" * 50)
        print("         LISTADO DE EXPEDIENTES Y TRÁMITES")
        print("=" * 50)

        for t in tramites:
            print(f"Código: {t[0]} | Datos: {t}")

        print("=" * 50)


def ordenar_tramites_por_codigo():
    tramites = obtener_todos_los_tramites()

    if len(tramites) == 0:
        print("\nNo hay trámites registrados para ordenar.")
        return

    print("\n--- Opciones de Ordenamiento ---")
    print("1. Ascendente (Menor a Mayor)")
    print("2. Descendente (Mayor a Menor)")

    # Validar la opción ingresada
    while True:
        opcion_ord = input("Seleccione una opción (1-2): ").strip()

        if opcion_ord == "1" or opcion_ord == "2":
            break

        print("Opción inválida. Ingrese 1 o 2.")

    n = len(tramites)

    for i in range(n):
        for j in range(0, n - i - 1):
            num1 = int(tramites[j][0][5:])
            num2 = int(tramites[j + 1][0][5:])

            if opcion_ord == "1":
                if num1 > num2:
                    temporal = tramites[j]
                    tramites[j] = tramites[j + 1]
                    tramites[j + 1] = temporal

            elif opcion_ord == "2":
                if num1 < num2:
                    temporal = tramites[j]
                    tramites[j] = tramites[j + 1]
                    tramites[j + 1] = temporal

   
    
    print("\n" + "=" * 120)

    if opcion_ord == "2":
        print("TRÁMITES ORDENADOS DESCENDENTEMENTE")
    else:
        print("TRÁMITES ORDENADOS ASCENDENTEMENTE")

    print("=" * 120)

    separador = "  |  "

    encabezados = [
        "CÓDIGO",
        "RESUMEN",
        "NOMBRE COMPLETO",
        "FUNDAMENTACIÓN",
        "DOCUMENTOS",
        "FECHA",
        "ESTADO"
    ]

    print(separador.join(encabezados))
    print("-" * 120)

    for t in tramites:
        if len(t) >= 7:
            datos = [
                t[0],
                t[1],
                t[2],
                t[3],
                t[4],
                t[5],
                t[6]
            ]

            print(separador.join(datos))
        else:
            print(f"Registro incompleto: {t}")

    print("=" * 120)
