# Formulario de Solicitudes

def formulario_solicitud():
    print("REGISTRO DE SOLICITUD")

    while True:
        apellido_paterno = input("\nIngrese su apellido paterno: ").strip()
        apellido_materno = input("Ingrese su apellido materno: ").strip()
        nombres = input("Ingrese sus nombres: ").strip()
        razon_social = input("Razon social: ").strip()
        documento = input("Ingrese su DNI: ").strip()

        if apellido_paterno == "" or apellido_materno == "" or nombres == "" or razon_social == "" or documento == "":
            print("Los campos no deben estar vacíos, complete los campos nuevamente.")
            continue 

        if len(documento) != 8 or not documento.isdigit():
            print("Dni no valido, intente nuevamente.")
            continue 
        print("\nDatos registrados correctamente")
        

def direccion():
    while True:
        print("\nEscriba el tipo de via:")
        print("1. Avenida")
        print("2. Jiron")
        print("3. Calle")
        print("4. Pasaje")
        print("5. Carretera")
        print("6. Prolongacion")

        Direccion = input("tipo de via: ").strip()

        if Direccion == "1":
            tipo_via = "Avenida"
            tipo = input("Ingrese el tipo de zona: ").strip()
            nombre_zona = input("Ingrese nombre de la zona: ").strip()
            referencia = input("Referencia: ").strip()
            departamento = input("Departamento: ").strip()
            provincia = input("Provincia: ").strip()
            distrito = input("Distrito: ").strip()

        elif Direccion == "2":
            tipo_via = "Jiron"
            tipo = input("Ingrese el tipo de zona: ").strip()
            nombre_zona = input("Ingrese nombre de la zona: ").strip()
            referencia = input("Referencia: ").strip()
            departamento = input("Departamento: ").strip()
            provincia = input("Provincia: ").strip()
            distrito = input("Distrito: ").strip()

        elif Direccion == "3":
            tipo_via = "Calle"
            tipo = input("Ingrese el tipo de zona: ").strip()
            nombre_zona = input("Ingrese nombre de la zona: ").strip()
            referencia = input("Referencia: ").strip()
            departamento = input("Departamento: ").strip()
            provincia = input("Provincia: ").strip()
            distrito = input("Distrito: ").strip()

        elif Direccion == "4":
            tipo_via = "Pasaje"
            tipo = input("Ingrese el tipo de zona: ").strip()
            nombre_zona = input("Ingrese nombre de la zona: ").strip()
            referencia = input("Referencia: ").strip()
            departamento = input("Departamento: ").strip()
            provincia = input("Provincia: ").strip()
            distrito = input("Distrito: ").strip()

        elif Direccion == "5":
            tipo_via = "Carretera"
            tipo = input("Ingrese el tipo de zona: ").strip()
            nombre_zona = input("Ingrese nombre de la zona: ").strip()
            referencia = input("Referencia: ").strip()
            departamento = input("Departamento: ").strip()
            provincia = input("Provincia: ").strip()
            distrito = input("Distrito: ").strip()

        elif Direccion == "6":
            tipo_via = "Prolongacion"
            tipo = input("Ingrese el tipo de zona: ").strip()
            nombre_zona = input("Ingrese nombre de la zona: ").strip()
            referencia = input("Referencia: ").strip()
            departamento = input("Departamento: ").strip()
            provincia = input("Provincia: ").strip()
            distrito = input("Distrito: ").strip()

        else:
            print("Tipo de via no valida, intente nuevamente.")
            continue  


datos_personales = formulario_solicitud()
datos_direccion = direccion()

print("\n--- REGISTRO COMPLETADO ---")
print("Datos personales:", datos_personales)
print("Dirección:", datos_direccion)
