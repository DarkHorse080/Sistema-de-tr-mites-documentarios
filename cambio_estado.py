from operaciones import convertir_a_lista, convertir_a_texto
from pathlib import Path
def cambiar_estado():
    """Modifica el estado de un trámite según su código.

    Propósito:
        Busca un trámite por su código en "Trámites.txt", permite elegir un nuevo estado (Enviado, En proceso o Completado), lo cambia y actualiza el archivo.

    Parámetros:
        Ninguno.

    Retorna:
        No devuelve ningún valor.

    Condiciones:
        Si el archivo no existe o está vacío finaliza.
        Si el código no se encuentra, se permanece en el bucle y se muestra un mensaje de no encontrado.
    """
    carpeta = Path(__file__).resolve().parent
    ruta = carpeta / "Trámites.txt"
    if not ruta.exists():
        print("No hay tramites registrados.")
        return

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    if not lineas:
        print("No hay tramites registrados.")
        return
    
    while True:
        codigo = input("Código: ").strip()
        encontrado = False
        nuevas_lineas = []
        for linea in lineas:
            linea = convertir_a_lista(linea)
            if codigo == linea[0]:
                encontrado = True
                while True:
                    print("----ESTADOS----")
                    print("1. Enviado")
                    print("2. En proceso")
                    print("3. Completado")
                    opcion_estado = input("Nuevo estado: ").strip()
                    if opcion_estado == "1":
                        nuevo_estado = "Enviado"
                        break
                    elif opcion_estado == "2":
                        nuevo_estado = "En proceso"
                        break
                    elif opcion_estado == "3":
                        nuevo_estado = "Completado"
                        break
                    else:
                        print("Opción no válida")
                linea[-1] = nuevo_estado
                nuevas_lineas.append(convertir_a_texto(linea))
                
            else:
                linea[-1] = linea[-1].strip()
                nuevas_lineas.append(convertir_a_texto(linea))

        if encontrado:
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write("\n".join(nuevas_lineas))
            print("Estado cambiado correctamente")
            break
        else:
            print("Trámite no encontrado")

