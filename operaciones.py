from pathlib import Path
from datetime import datetime

def convertir_a_texto(lista):
    """Convierte una lista de elementos en una cadena de texto separada por punto y coma.

    Propósito:
        Une los elementos de una lista utilizando ';' como delimitador para facilitar su almacenamiento en archivos de texto.

    Parámetros:
        Lista de elementos a convertir.

    Retorna:
        Cadena de texto resultante con los elementos unidos por punto y coma.

    Condiciones:
        Ninguna.
    """
    return ";".join(lista)


def convertir_a_lista(texto):
    """Convierte una cadena de texto delimitada por punto y coma en una lista.

    Propósito:
        Separa una línea de texto leída del archivo utilizando ';' para 
        recuperar los datos estructurados en formato de lista.

    Parámetros:
        Cadena de texto con elementos separados por punto y coma.

    Retorna:
        Lista con los elementos individuales extraídos del texto.

    Condiciones:
        Ninguna.
    """
    return texto.split(";")


def obtener_todos_los_tramites():
    """Lee y carga todos los trámites registrados desde el archivo de texto.

    Propósito:
        Busca el archivo "Trámites.txt" en el directorio actual, lee su contenido línea por línea, omite líneas vacías y convierte cada registro en una lista.

    Parámetros:
        Ninguno.

    Retorna:
        Una lista de listas, donde cada sublista contiene los datos de un trámite. 
        Retorna una lista vacía si el archivo no existe.

    Condiciones:
        Si el archivo "Trámites.txt" no existe, retorna una lista vacía.
        Emplea la codificación "utf-8-sig".
    """
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
    """Ajusta una cadena de texto a un ancho fijo para mantener formato tabular.

    Propósito:
        Reduce el texto añadiendo puntos suspensivos ("...") si excede el ancho 
        permitido, o rellena con espacios en blanco a la derecha si es más corto.

    Parámetros:
        texto (str): El texto que se desea ajustar.
        ancho (int): El ancho máximo de caracteres permitidos para la columna.

    Retorna:
        Cadena de texto formateada exactamente con la longitud del ancho especificado.

    Condiciones:
        Si la longitud del texto supera el ancho, corta el contenido en `ancho - 3` 
        y concatena "...".
    """
    texto = str(texto)
    if len(texto) > ancho:
        return texto[: ancho - 3] + "..."
    return texto.ljust(ancho)

def mostrar_tramites(tramites):
    """Muestra por consola una tabla formateada con los trámites proporcionados.

    Propósito:
        Recibe una lista de trámites, valida la estructura de cada registro 
        (según el número de elementos sea 20 para jurídica o 22 para natural) 
        y los imprime en columnas alineadas con sus respectivos encabezados.

    Parámetros:
        tramites (list): Lista de listas con la información de los trámites a mostrar.

    Retorna:
        Nada.

    Condiciones:
        Evalúa si la longitud de la lista del trámite `t` es 20 (persona jurídica) 
        o 22 (persona natural) para extraer y mostrar los campos correspondientes.
    """
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
    """Gestiona y presenta todos los trámites.

    Propósito:
        Obtiene todos los registros mediante `obtener_todos_los_tramites()`, comprueba 
        si existen datos y muestra la cabecera junto con la tabla de trámites.

    Parámetros:
        Ninguno.

    Retorna:
        Nada.

    Condiciones:
        Si la lista de trámites está vacía, imprime un mensaje indicando que no hay 
        registros en el sistema.
    """
    tramites = obtener_todos_los_tramites()

    if len(tramites) == 0:
        print("\nNo hay trámites registrados en el sistema.")
    else:
        print("\n" + "=" * 146)
        print(" "*56 + "LISTADO DE EXPEDIENTES Y TRÁMITES")
        print("=" * 146)
        mostrar_tramites(tramites)
        print("=" * 146)