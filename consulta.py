
from pathlib import Path


def consultar_tramite():
    print("\n--- CONSULTA DE TRAMITES ---")

    codigo = input("Ingrese el codigo del tramite: ").strip()

    if not codigo:
        print("Debe ingresar un codigo.")
        return

    carpeta = Path(__file__).resolve().parent
    ruta = carpeta / "Tr\u00e1mites.txt"

    if not ruta.exists():
        ruta = carpeta / "Tramites.txt"

    if not ruta.exists():
        print("No se encontro el archivo de tramites.")
        print("Crea el archivo al registrar el primer tramite.")
        return

    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue

            datos = linea.strip().split(";")

            if datos[0].strip() != codigo:
                continue

            print("\n========== TRAMITE ENCONTRADO ==========")
            print("Codigo:", datos[0])
            print("Resumen del pedido:", datos[1])
            print("Autoridad:", datos[2])

            if len(datos) == 22:
                print("\n--- DATOS DEL SOLICITANTE ---")
                print("Tipo de persona:", datos[3])
                print("Apellido paterno:", datos[4])
                print("Apellido materno:", datos[5])
                print("Nombres:", datos[6])
                print("DNI:", datos[7])
                print("Correo:", datos[8])
                print("Telefono:", datos[9])
                inicio = 10

            elif len(datos) == 20:
                print("\n--- DATOS DE LA EMPRESA ---")
                print("Tipo de persona:", datos[3])
                print("Razon social:", datos[4])
                print("RUC:", datos[5])
                print("Correo:", datos[6])
                print("Telefono:", datos[7])
                inicio = 8

            else:
                print("\nNo se reconoce la estructura del registro.")
                print("Cantidad de campos encontrados:", len(datos))
                print("Registro completo:", datos)
                return

            nombres_direccion = [
                "Departamento",
                "Provincia",
                "Distrito",
                "Tipo de via",
                "Nombre de via",
                "Numero",
                "Interior",
                "Referencia"
            ]

            print("\n--- DIRECCION ---")
            for i, nombre in enumerate(nombres_direccion):
                print(nombre + ":", datos[inicio + i])

            inicio_final = inicio + 8

            print("\n--- DETALLES DEL TRAMITE ---")
            print("Fundamentacion:", datos[inicio_final])
            print("Documentos adjuntos:", datos[inicio_final + 1])
            print("Fecha:", datos[inicio_final + 2])
            print("Estado:", datos[inicio_final + 3])
            print("========================================")
            return

    print("\nNo se encontro un tramite con ese codigo.")


if __name__ == "__main__":
    consultar_tramite()
