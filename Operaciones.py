from pathlib import Path
from datetime import datetime

def convertir_a_texto(lista):
    return ";".join(lista)


def convertir_a_lista(texto):
    return texto.split(";")


def obtener_todos_los_tramites():
    ruta = Path("Trámites.txt")

    if not ruta.exists():
        return []

    with open(ruta, "r", encoding="utf-8-sig") as tramites:
        lineas = tramites.readlines()
    
    lista_tramites = []

    for linea in lineas:
        linea_limpia = linea.strip()

        if linea_limpia != "":
            datos = convertir_a_lista(linea_limpia)
            lista_tramites.append(datos)

    return lista_tramites


def ajustar_texto(texto, ancho):
    texto = str(texto)
    if len(texto) > ancho:
        return texto[: ancho - 3] + "..."
    return texto.ljust(ancho)


def mostrar_todos_los_tramites():
    tramites = obtener_todos_los_tramites()

    if len(tramites) == 0:
        print("\nNo hay trámites registrados en el sistema.")
    else:
        print("\n" + "=" * 146)
        print(" "*56 + "LISTADO DE EXPEDIENTES Y TRÁMITES")
        print("=" * 146)

        separador = "  |  "
        
        anchos = [10, 15, 31, 25, 15, 10, 10]
        
        encabezados = [
            "CÓDIGO",
            "RESUMEN",
            "NOMBRE / RAZÓN SOCIAL",
            "FUNDAMENTACIÓN",
            "DOCUMENTOS",
            "FECHA",
            "ESTADO"
        ]
    
        
        linea_encabezados = separador.join([encabezados[i].ljust(anchos[i]) for i in range(len(encabezados))])
        print(linea_encabezados)
        print("-" * len(linea_encabezados))
        for t in tramites:
            if len(t) == 20:
                datos = [
                    ajustar_texto(t[0], anchos[0]),
                    ajustar_texto(t[1], anchos[1]),
                    ajustar_texto(t[4], anchos[2]),
                    ajustar_texto(t[16], anchos[3]),
                    ajustar_texto(t[17], anchos[4]),
                    ajustar_texto(t[18], anchos[5]),
                    ajustar_texto(t[19], anchos[6])
                ]
                print(separador.join(datos))
            elif len(t) == 22:
                nombre_completo = f"{t[4]} {t[5]} {t[6]}"
                datos = [
                    ajustar_texto(t[0], anchos[0]),
                    ajustar_texto(t[1], anchos[1]),
                    ajustar_texto(nombre_completo, anchos[2]),
                    ajustar_texto(t[18], anchos[3]),
                    ajustar_texto(t[19], anchos[4]),
                    ajustar_texto(t[20], anchos[5]),
                    ajustar_texto(t[21], anchos[6])
                ]
                print(separador.join(datos))

        print("=" * 146)


def ordenar_tramites_por_codigo():
    tramites = obtener_todos_los_tramites()

    if len(tramites) == 0:
        print("\nNo hay trámites registrados para ordenar.")
        return

    print("\n--- Opciones de Ordenamiento ---")
    print("1. Ascendente (Menor a Mayor)")
    print("2. Descendente (Mayor a Menor)")

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

    print("\n" + "=" * 146)

    if opcion_ord == "2":
        print("TRÁMITES ORDENADOS DESCENDENTEMENTE")
    else:
        print("TRÁMITES ORDENADOS ASCENDENTEMENTE")

    print("=" * 146)

    separador = "  |  "
    anchos = [10, 15, 31, 25, 15, 10, 10]

    encabezados = [
        "CÓDIGO",
        "RESUMEN",
        "NOMBRE / RAZÓN SOCIAL",
        "FUNDAMENTACIÓN",
        "DOCUMENTOS",
        "FECHA",
        "ESTADO"
    ]

    linea_encabezados = separador.join([encabezados[i].ljust(anchos[i]) for i in range(len(encabezados))])
    print(linea_encabezados)
    print("-" * len(linea_encabezados))

    for t in tramites:
        if len(t) == 20:
            datos = [
                ajustar_texto(t[0], anchos[0]),
                ajustar_texto(t[1], anchos[1]),
                ajustar_texto(t[4], anchos[2]),
                ajustar_texto(t[16], anchos[3]),
                ajustar_texto(t[17], anchos[4]),
                ajustar_texto(t[18], anchos[5]),
                ajustar_texto(t[19], anchos[6])
            ]
            print(separador.join(datos))
        elif len(t) == 22:
            nombre_completo = f"{t[4]} {t[5]} {t[6]}"
            datos = [
                ajustar_texto(t[0], anchos[0]),
                ajustar_texto(t[1], anchos[1]),
                ajustar_texto(nombre_completo, anchos[2]),
                ajustar_texto(t[18], anchos[3]),
                ajustar_texto(t[19], anchos[4]),
                ajustar_texto(t[20], anchos[5]),
                ajustar_texto(t[21], anchos[6])
            ]
            print(separador.join(datos))
        else:
            print(f"Registro incompleto: {t}")

    print("=" * 146)

def ordenar_tramites_por_fecha():
    tramites = obtener_todos_los_tramites()

    if len(tramites) == 0:
        print("\nNo hay trámites registrados para ordenar.")
        return

    n = len(tramites)

    for i in range(n):
        for j in range(0, n - i - 1):

            fecha1 = tramites[j][-2]
            fecha2 = tramites[j + 1][-2]

            dia1 = int(fecha1[0:2])
            mes1 = int(fecha1[3:5])
            anio1 = int(fecha1[6:10])

            dia2 = int(fecha2[0:2])
            mes2 = int(fecha2[3:5])
            anio2 = int(fecha2[6:10])

            if anio1 > anio2:
                temporal = tramites[j]
                tramites[j] = tramites[j + 1]
                tramites[j + 1] = temporal
            elif anio1 == anio2:
                if mes1 > mes2:
                    temporal = tramites[j]
                    tramites[j] = tramites[j + 1]
                    tramites[j + 1] = temporal
                elif mes1 == mes2:
                    if dia1 > dia2:
                        temporal = tramites[j]
                        tramites[j] = tramites[j + 1]
                        tramites[j + 1] = temporal

    print("\n" + "=" * 146)
    print("TRÁMITES ORDENADOS POR FECHA")
    print("=" * 146)

    separador = "  |  "
    anchos = [10, 15, 31, 25, 15, 10, 10]
    encabezados = ["CÓDIGO", "RESUMEN", "NOMBRE / RAZÓN SOCIAL", "FUNDAMENTACIÓN", "DOCUMENTOS", "FECHA", "ESTADO"]

    linea_encabezados = separador.join([encabezados[i].ljust(anchos[i]) for i in range(len(encabezados))])
    print(linea_encabezados)
    print("-" * len(linea_encabezados))

    for t in tramites:
        if len(t) == 20:
            datos = [
                ajustar_texto(t[0], anchos[0]),
                ajustar_texto(t[1], anchos[1]),
                ajustar_texto(t[4], anchos[2]),
                ajustar_texto(t[16], anchos[3]),
                ajustar_texto(t[17], anchos[4]),
                ajustar_texto(t[18], anchos[5]),
                ajustar_texto(t[19], anchos[6])
            ]
            print(separador.join(datos))
        elif len(t) == 22:
            nombre_completo = f"{t[4]} {t[5]} {t[6]}"
            datos = [
                ajustar_texto(t[0], anchos[0]),
                ajustar_texto(t[1], anchos[1]),
                ajustar_texto(nombre_completo, anchos[2]),
                ajustar_texto(t[18], anchos[3]),
                ajustar_texto(t[19], anchos[4]),
                ajustar_texto(t[20], anchos[5]),
                ajustar_texto(t[21], anchos[6])
            ]
            print(separador.join(datos))
        else:
            print(f"Registro incompleto: {t}")

    print("=" * 146)



def ordenar_tramites_por_estado():
    tramites = obtener_todos_los_tramites()
    if len(tramites) == 0:
        print("\nNo hay trámites registrados para ordenar.")
        return

    orden_estados = {
        "Enviado": 1,
        "En proceso": 2,
        "Completado": 3
    }

    n = len(tramites)

    for i in range(n):
        for j in range(0, n - i - 1):
            estado1 = tramites[j][-1]
            estado2 = tramites[j + 1][-1]

            valor1 = orden_estados.get(estado1, 99)
            valor2 = orden_estados.get(estado2, 99)

            if valor1 > valor2:
                temporal = tramites[j]
                tramites[j] = tramites[j + 1]
                tramites[j + 1] = temporal

    print("\n" + "=" * 146)
    print("TRÁMITES ORDENADOS POR ESTADO")
    print("=" * 146)

    separador = "  |  "
    anchos = [10, 15, 31, 25, 15, 10, 10]
    encabezados = ["CÓDIGO", "RESUMEN", "NOMBRE / RAZÓN SOCIAL", "FUNDAMENTACIÓN", "DOCUMENTOS", "FECHA", "ESTADO"]

    linea_encabezados = separador.join([encabezados[i].ljust(anchos[i]) for i in range(len(encabezados))])
    print(linea_encabezados)
    print("-" * len(linea_encabezados))

    for t in tramites:
        if len(t) == 20:
            datos = [
                ajustar_texto(t[0], anchos[0]),
                ajustar_texto(t[1], anchos[1]),
                ajustar_texto(t[4], anchos[2]),
                ajustar_texto(t[16], anchos[3]),
                ajustar_texto(t[17], anchos[4]),
                ajustar_texto(t[18], anchos[5]),
                ajustar_texto(t[19], anchos[6])
            ]
            print(separador.join(datos))
        elif len(t) == 22:
            nombre_completo = f"{t[4]} {t[5]} {t[6]}"
            datos = [
                ajustar_texto(t[0], anchos[0]),
                ajustar_texto(t[1], anchos[1]),
                ajustar_texto(nombre_completo, anchos[2]),
                ajustar_texto(t[18], anchos[3]),
                ajustar_texto(t[19], anchos[4]),
                ajustar_texto(t[20], anchos[5]),
                ajustar_texto(t[21], anchos[6])
            ]
            print(separador.join(datos))
        else:
            print(f"Registro incompleto: {t}")

    print("=" * 146)

def ordenar():
      print("\n--- Opciones de Ordenamiento ---")
      print("1. Ordenar por Código")
      print("2. Ordenar por Fecha")
      print("3. Ordenar por Estado")
   
      while True:
         opcion = input("Seleccione una opción (1-3): ").strip()
   
         if opcion == "1":
               ordenar_tramites_por_codigo()
               break
         elif opcion == "2":
               ordenar_tramites_por_fecha()
               break
         elif opcion == "3":
               ordenar_tramites_por_estado()
               break
         else:
               print("Opción inválida. Ingrese un número entre 1 y 3.")

