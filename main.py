from consulta import consultar_tramite
from Formulario_Trámite import Formulario_Unico_de_Trámite
from Registro_tramite import Registrar_Tramite
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

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        match opcion:
            case "1":
                print("\n[Módulo de Registro]")
                Registrar_Tramite(Formulario_Unico_de_Trámite())
            case "2":
                print("\n[Módulo de Consulta]")
                consultar_tramite()
            case "3":
                print("\n[Módulo de Ordenamiento]")
            case "4":
                print("\n[Módulo de Listado]")
            case "5":
                print("\n¡Saliendo del sistema Mesa de Partes Digital!")
                break
            case _:
                print("\nOpción no válida. Ingrese un número entre 1 y 5.")

main()