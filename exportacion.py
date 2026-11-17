import csv

def exportar_csv():
    """Exporta los datos de los trámites almacenados en texto plano a un formato CSV.

    Propósito:
        Lee el archivo de texto "Trámites.txt" delimitado por punto y coma (";") y genera un nuevo archivo "Trámites.csv" compatible con hojas de cálculo.

    Parámetros:
        Ninguno.

    Retorna:
        Nada.

    Condiciones:
        Si el archivo "Trámites.txt" no existe, captura la excepción FileNotFoundError y muestra un mensaje indicando que no se encontró el archivo.
    """
    try:
        with open("Trámites.txt", "r", encoding="utf-8") as archivo_txt:
            lector = csv.reader(archivo_txt, delimiter=";")

            with open("Trámites.csv", "w", newline="", encoding="utf-8") as archivo_csv:
                escritor = csv.writer(archivo_csv)

                for fila in lector:
                    escritor.writerow(fila)

        print("¡Archivo CSV exportado correctamente!")

    except FileNotFoundError:
        print("No se encontró el archivo Trámites.txt")
