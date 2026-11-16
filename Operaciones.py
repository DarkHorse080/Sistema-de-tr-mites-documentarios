from pathlib import Path
from datetime import datetime

def convertir_a_texto(lista):
    return ";".join(lista)


def convertir_a_lista(texto):
    return texto.split(";")


def obtener_todos_los_tramites():
    carpeta = Path(__file__).resolve().parent
    ruta = carpeta / "Trámites.txt"
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

def mostrar_tramites(tramites):
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

def mostrar_todos_los_tramites():
    tramites = obtener_todos_los_tramites()

    if len(tramites) == 0:
        print("\nNo hay trámites registrados en el sistema.")
    else:
        print("\n" + "=" * 146)
        print(" "*56 + "LISTADO DE EXPEDIENTES Y TRÁMITES")
        print("=" * 146)
        mostrar_tramites(tramites)
        print("=" * 146)


