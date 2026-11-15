from Operaciones import obtener_todos_los_tramites

def generar_reporte():
    tramites = obtener_todos_los_tramites()
    
    if len(tramites) == 0:
        print("\nNo hay tramites registrados.")
        return

    dni_cont = 0
    razon_social_cont = 0

    for t in tramites:
        texto = " ".join(t).upper()
        if "DNI" in texto:
            dni_cont += 1
        else:
            razon_social_cont += 1

    print("\n--- REPORTE DE TRAMITES ---")
    print(f"Con DNI: {dni_cont}")
    print(f"Con Razón Social: {razon_social_cont}")
    print(f"Total: {len(tramites)}")
    print("-" * 30)