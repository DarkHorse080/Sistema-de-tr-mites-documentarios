from operaciones import obtener_todos_los_tramites

def generar_reporte():
    tramites = obtener_todos_los_tramites()
    
    if len(tramites) == 0:
        print("\nNo hay tramites registrados.")
        return

    natural_cont = 0
    juridica_cont = 0

    for t in tramites:
        tipo_persona = str(t[3]).strip().upper()
        if tipo_persona == "NATURAL":
            natural_cont += 1
        else:
            juridica_cont += 1

    print("\n--- REPORTE DE TRAMITES ---")
    print(f"Persona Natural: {natural_cont}")
    print(f"Persona Jurídica: {juridica_cont}")
    print(f"Total: {len(tramites)}")
    print("-" * 30)