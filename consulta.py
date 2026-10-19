
from pathlib import Path
from Operaciones import convertir_a_lista


def consultar_tramite():
    print("\n--- CONSULTA DE TRAMITES ---")

    codigo = input("Ingrese el codigo del tramite: ").strip()

    if not codigo:
        print("Debe ingresar un codigo.")
        return

    ruta = Path("Trámites.txt")

    if not ruta.exists():
        print("Todavia no hay tramites registrados.")
        return

    encontrado = False

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue

            datos = convertir_a_lista(linea.strip())

            if datos[0] == codigo:
                print("\n--- TRAMITE ENCONTRADO ---")
                print("Codigo:", datos[0])
                print("Resumen del pedido:", datos[1])
                print("Autoridad:", datos[2])
                print("Datos del solicitante:", datos[3:10])
                print("Direccion:", datos[10:18])
                print("Fundamentacion:", datos[18])
                print("Documentos adjuntos:", datos[19])
                print("Fecha:", datos[20])
                print("Estado:", datos[21])

                encontrado = True
                break

    if not encontrado:
        print("No se encontro el tramite.")


if __name__ == "__main__":
    consultar_tramite()
