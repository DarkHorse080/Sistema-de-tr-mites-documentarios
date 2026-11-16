from operaciones import obtener_todos_los_tramites,mostrar_tramites
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

    mostrar_tramites(tramites)

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

    mostrar_tramites(tramites)

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

    mostrar_tramites(tramites)

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

