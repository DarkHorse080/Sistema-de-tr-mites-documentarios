# Listas paralelas
codigos = []
nombres = []
asuntos = []
fechas = []          

def mostrar_menu():
    print("\n" + "="*45)
    print("  MESA DE PARTES DIGITAL - I.E. 1.4.8")
    print("="*45)
    print("1. Registrar nuevo expediente")
    print("2. Consultar expediente (DNI / Código)")
    print("3. Ordenar expedientes")
    print("4. Mostrar todos los expedientes")
    print("5. Salir")
    print("="*45)


def registrar_expendiente(): 
    
    dni = input("Ingrese el DNI (8 dígitos): ").strip()
    nombre = input("Ingrese nombres y apellidos: ").strip()
    asunto = input("Ingrese el asunto del trámite: ").strip()
    fecha = input("Ingrese la fecha (dd/mm/aa): ").strip()

    # Validaciones
    if len(dni) != 8 or not dni.isdigit():
        print("Dni no valido")
        return

    if dni == "" or nombre == "" or asunto == "" or fecha == "":
        print("Por favor complete los datos")
        return

    # Guardar en las listas
    codigos.append(dni)
    nombres.append(nombre)
    asuntos.append(asunto)
    fechas.append(fecha)

    print("\n¡Expediente registrado con éxito!")
    print("Código (DNI):", dni)
    print("Nombre      :", nombre)
    print("Asunto      :", asunto)
    print("Fecha       :", fecha)


def consultar_expediente():
    if len(codigos) == 0:
        print("\nNo hay expedientes registrados.")
        return

    print("\nConsulta de Expediente")    
    print("1. Buscar por Código (DNI)")
    print("2. Buscar por Nombre")
    opcion = input("Elija una opción (1 o 2): ").strip()

    encontrado = False          # Antes tenías "encontrar"

    if opcion == "1":
        buscar = input("Ingrese codigo (DNI): ").strip()
        for i in range(len(codigos)):
            if codigos[i] == buscar:
                print("\nExpediente encontrado")
                print("Código (DNI):", codigos[i])
                print("Nombre      :", nombres[i])
                print("Asunto      :", asuntos[i])
                print("Fecha       :", fechas[i])
                encontrado = True
                break

    elif opcion == "2":
        estudiante = input("Ingrese el nombre del estudiante: ").strip()
        for i in range(len(codigos)):
            if estudiante.lower() in nombres[i].lower():
                print("\nExpediente encontrado")
                print("Código (DNI):", codigos[i])
                print("Nombre      :", nombres[i])
                print("Asunto      :", asuntos[i])
                print("Fecha       :", fechas[i])
                encontrado = True
                break
    else:
        print("Opcion no valida")
        return

    if not encontrado:
        print("\nNo se encontró ningún expediente")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            print("\n[Módulo de Registro]") 
            registrar_expendiente()            
        elif opcion == "2":
            print("\n[Módulo de Consulta]") 
            consultar_expediente()
        elif opcion == "3":
            print("\n[Módulo de Ordenamiento]")  # Falta hacer
        elif opcion == "4":
            print("\n[Módulo de Listado]")      # Falta hacer
        elif opcion == "5":
            print("\n¡Saliendo del sistema Mesa de Partes Digital!")
            break
        else:
            print("\nOpción no válida. Ingrese un número entre 1 y 5.")

main()
