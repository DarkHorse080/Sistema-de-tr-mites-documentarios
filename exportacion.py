import csv

def exportar_csv():
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
