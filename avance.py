# Formulario de Solicitudes
def formulario_solicitud():
    print("REGISTRO DE SOLICITUD")
    while True:
        print("\nTipo de persona")
        print("1. Persona Natural")
        print("2. Persona Juridica")
        tipo_persona = input("Elija una opción (1 o 2): ").strip()

        if tipo_persona == "1":
            persona = "Natural"
            apellido_paterno = input("\nIngrese su apellido paterno: ").strip()
            apellido_materno = input("Ingrese su apellido materno: ").strip()
            nombres = input("Ingrese sus nombres: ").strip()
            razon_social = ""
        elif tipo_persona == "2":
            persona = "Juridica"
            apellido_paterno = ""
            apellido_materno = ""
            nombres = ""
            razon_social = input("\nIngrese la Razón Social: ").strip()
        else:
            print("Operacion no valida, intetelo nuevamente")
            continue

        documento = input("Ingrese su DNI/RUC: ").strip()
        correo = input("Ingrese su correo electronico: ").strip()
        telefono = input("Ingrese su teléfono: ").strip()

        if (not documento or not correo or not telefono or
                (persona == "Natural" and not all((apellido_paterno, apellido_materno, nombres))) or
                (persona == "Juridica" and not razon_social)):
            print("Los campos no deben estar vacíos, complete los campos nuevamente.")
            continue

        if persona == "Natural" and (len(documento) != 8 or not documento.isdigit()):
            print("Dni no valido, intente nuevamente.")
            continue

        print("\nDatos registrados correctamente")
        return [persona, apellido_paterno, apellido_materno, nombres, razon_social, documento, correo, telefono]
''
def direccion():
    while True:
        print("\n elija el tipo de via:")
        print("1. Avenida")
        print("2. Jiron")
        print("3. Calle")
        print("4. Pasaje")
        print("5. Carretera")
        print("6. Prolongacion")

        Direccion = input("tipo de via: ").strip()

        if Direccion == "1":
            tipo_via = "Avenida"
        elif Direccion == "2":
            tipo_via = "Jiron"
        elif Direccion == "3":
            tipo_via = "Calle"
        elif Direccion == "4":
            tipo_via = "Pasaje"
        elif Direccion == "5":
            tipo_via = "Carretera"
        elif Direccion == "6":
            tipo_via = "Prolongacion"
        else:
            print("Tipo de via no valida, intente nuevamente.")
            continue  
        tipo = input("Ingrese el tipo de zona: ").strip()
        nombre_zona = input("Ingrese nombre de la zona: ").strip()
        referencia = input("Referencia: ").strip()
        departamento = input("Departamento: ").strip()
        provincia = input("Provincia: ").strip()
        distrito = input("Distrito: ").strip()
        return [tipo_via, tipo, nombre_zona, referencia, departamento, provincia, distrito]


datos_personales = formulario_solicitud()
datos_direccion = direccion()

print("\n--- REGISTRO COMPLETADO ---")
print("\nDatos personales:")
print("Tipo de persona :", datos_personales[0])
print("Apellido paterno:", datos_personales[1])
print("Apellido materno:", datos_personales[2])
print("Nombres         :", datos_personales[3])
print("Razón social    :", datos_personales[4])
print("Documento       :", datos_personales[5])
print("Correo          :", datos_personales[6])
print("Teléfono        :", datos_personales[7])

print("\nDirección:")
print("Tipo de vía     :", datos_direccion[0])
print("Tipo de zona    :", datos_direccion[1])
print("Nombre de zona  :", datos_direccion[2])
print("Referencia      :", datos_direccion[3])
print("Departamento    :", datos_direccion[4])
print("Provincia       :", datos_direccion[5])
print("Distrito        :", datos_direccion[6])
