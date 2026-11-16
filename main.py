from consulta import consultar_tramite
from Formulario_Trámite import Formulario_Unico_de_Trámite
from Registro_tramite import Registrar_Tramite
from Operaciones import mostrar_todos_los_tramites, ordenar
from reportes import generar_reporte
from cambio_estado import cambiar_estado
from exportacion import exportar_csv
def mostrar_menu():
    print("\n" + "="*45)
    print("  MESA DE PARTES DIGITAL - I.E. 1.4.8")
    print("="*45)
    print("1. Registrar nuevo expediente")
    print("2. Consultar expediente (DNI / Código)")
    print("3. Ordenar expedientes")
    print("4. Mostrar todos los expedientes")
    print("5. Generar reporte de solicitantes")
    print("6. Cambiar estado del trámite")
    print("7. Exportar a CSV")
    print("8. Salir")
    print("="*45)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()

        match opcion:
            case "1":
                print("\n[Módulo de Registro]")
                Registrar_Tramite(Formulario_Unico_de_Trámite())
            case "2":
                print("\n[Módulo de Consulta]")
                consultar_tramite()
            case "3":
                print("\n[Módulo de Ordenamiento]")
                ordenar()
            case "4":
                print("\n[Módulo de Listado]")
                mostrar_todos_los_tramites()
            case "5":
                print("\n[Módulo de Reportes]")
                generar_reporte()
            case "6":
                print("\n[Módulo de Cambio de Estado]")
                cambiar_estado()
            case "7":
                print("\n[Módulo de Exportación a CSV]")
                exportar_csv()
            case "8":
                print("\n¡Saliendo del sistema Mesa de Partes Digital!")
                break
            case _:
                print("\nOpción no válida. Ingrese un número entre 1 y 8.")

main()