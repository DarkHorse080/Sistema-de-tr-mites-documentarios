# Formulario de Solicitudes

def formulario_solicitud():
    print("REGISTRO DE SOLICITUD")

    apellido_paterno = input("Ingrese su apellido paterno: ").strip()
    apellido_materno = input("Ingrese su apellido materno: ").strip()
    nombres = input("Ingrese sus nombres: ").strip()
    razon_social = input("Razon social: ").strip()
    documento = input("Ingrese su DNI: ").strip()

    if apellido_paterno == "" or apellido_materno == "" or nombres == "" or razon_social == "" or documento == "":
        print("Los campos no deben estar vacíos, complete los campos")
        return apellido_paterno, apellido_materno, nombres, razon_social, documento
        

    
    if len(documento) != 8 or not documento.isdigit():
        print("Dni no valido")
        return documento

    else:
        print("\nDatos registrados correctamente")
        return apellido_paterno, apellido_materno, nombres, razon_social, documento


def direccion():
    print("Escriba el tipo de via:")
    print("1. Avenida")
    print("2. Jiron")
    print("3. Calle")
    print("4. Pasaje")
    print("5. Carretera")
    print("6. Prolongacion")

    Direccion = input("tipo de via: ")

    if Direccion == "1":
        tipo = input("Ingrese el tipo de zona: ")
        nombre_zona = input("Ingrese nombre de la zona: ")
        referencia = input("Referencia: ")
        departamento = input("Departamento: ")
        provincia = input("Provincia: ")
        distrito = input("Distrito: ")

    elif Direccion == "2":
        tipo = input("Ingrese el tipo de zona: ")
        nombre_zona = input("Ingrese nombre de la zona: ")
        referencia = input("Referencia: ")
        departamento = input("Departamento: ")
        provincia = input("Provincia: ")
        distrito = input("Distrito: ")

    elif Direccion == "3":
        tipo = input("Ingrese el tipo de zona: ")
        nombre_zona = input("Ingrese nombre de la zona: ")
        referencia = input("Referencia: ")
        departamento = input("Departamento: ")
        provincia = input("Provincia: ")
        distrito = input("Distrito: ")

    elif Direccion == "4":
        tipo = input("Ingrese el tipo de zona: ")
        nombre_zona = input("Ingrese nombre de la zona: ")
        referencia = input("Referencia: ")
        departamento = input("Departamento: ")
        provincia = input("Provincia: ")
        distrito = input("Distrito: ")

    elif Direccion == "5":
        tipo = input("Ingrese el tipo de zona: ")
        nombre_zona = input("Ingrese nombre de la zona: ")
        referencia = input("Referencia: ")
        departamento = input("Departamento: ")
        provincia = input("Provincia: ")
        distrito = input("Distrito: ")

    elif Direccion == "6":
        tipo = input("Ingrese el tipo de zona: ")
        nombre_zona = input("Ingrese nombre de la zona: ")
        referencia = input("Referencia: ")
        departamento = input("Departamento: ")
        provincia = input("Provincia: ")
        distrito = input("Distrito: ")

    else:
        print("Tipo de via no valida")
        return

    return tipo, nombre_zona, referencia, departamento, provincia, distrito

# Para probar:
formulario_solicitud()
direccion()

