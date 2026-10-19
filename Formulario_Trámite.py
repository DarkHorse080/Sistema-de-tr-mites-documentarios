import datetime
import re
def Resumen_del_pedido():
    while True:
        print("\nI. RESUMEN DE SU PEDIDO")
        resumen_pedido=input()
        if not resumen_pedido:
            print("El campo no puede estar vacío")
            continue

        return resumen_pedido
        

def Autoridad_a_la_que_se_dirige():
    
    while True:
        print("\nII. DEPENDENCIA O AUTORIDAD A LA QUE SE DIRIGE")
        autoridad=input()
        if not autoridad:
            print("El campo no puede estar vacío")
            continue
        return autoridad
def Datos_del_solicitante():
    print("\nIII. DATOS DEL SOLICITANTE")
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
            
        elif tipo_persona == "2":
            persona = "Juridica"
            
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

        if persona == "Juridica" and (len(documento) != 11 or not documento.isdigit()):
            print("RUC no valido, intente nuevamente.")
            continue

        if (len(telefono) != 9 or not telefono.isdigit()):
            print("Teléfono no valido, intente nuevamente.")
            continue

        if (not re.fullmatch(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$",correo)):
            print("Correo no valido, intente nuevamente.")
            continue

        if persona == "Natural":
            return [persona, apellido_paterno, apellido_materno, nombres, documento, correo, telefono]
        elif persona == "Juridica":
            return [persona, razon_social, documento, correo, telefono]
        
        

def Direccion():
    print("\nIV. DIRECCIÓN")
    while True:

        print("\n Elija el tipo de via:")
        print("1. Avenida")
        print("2. Jiron")
        print("3. Calle")
        print("4. Pasaje")
        print("5. Carretera")
        print("6. Prolongacion")

        Direccion = input("Tipo de via: ").strip()

        match Direccion:
            case "1":
                tipo_via = "Avenida"
            case "2":
                tipo_via = "Jiron"
            case "3":
                tipo_via = "Calle"
            case "4":
                tipo_via = "Pasaje"
            case "5":
                tipo_via = "Carretera"
            case "6":
                tipo_via = "Prolongacion"
            case _:
                print("Tipo de via no valida, intente nuevamente.")
                continue  
        nombre_via=input("Ingrese nombre de la via: ").strip()

        print("\n Elija el tipo de via:")
        print("1. Urbanización")
        print("2. Pueblo Joven")
        print("3. Unidad Vecinal")
        print("4. Conjunto Habitacional")
        print("5. Cooperativa")
        print("6. Residencial")
        print("7. Zona Industrial")
        print("8. Centro Poblado")
        print("9. Asociación")
        print("10. Grupo")
        print("11. Fundo")
        print("12. Otros")
        
        Direccion2 = input("Ingrese el tipo de zona: ").strip()

        match Direccion2:
                    case "1":
                        tipo_zona = "Urbanización"
                    case "2":
                        tipo_zona = "Pueblo Joven"
                    case "3":
                        tipo_zona = "Unidad Vecinal"
                    case "4":
                        tipo_zona = "Conjunto Habitacional"
                    case "5":
                        tipo_zona = "Cooperativa"
                    case "6":
                        tipo_zona = "Residencial"
                    case "7":
                        tipo_zona = "Zona Industrial"
                    case "8":
                        tipo_zona = "Centro Poblado"
                    case "9":
                        tipo_zona = "Asociación"
                    case "10":
                        tipo_zona = "Grupo"
                    case "11":
                        tipo_zona = "Fundo"
                    case "12":
                        tipo_zona = "Otros"
                    case _:
                        print("Tipo de zona no valida, intente nuevamente.")
                        continue  



        nombre_zona = input("Ingrese nombre de la zona: ").strip()
        referencia = input("Referencia: ").strip()
        departamento = input("Departamento: ").strip()
        provincia = input("Provincia: ").strip()
        distrito = input("Distrito: ").strip()


        if (not nombre_via or not nombre_zona or not referencia or not departamento or not provincia or not distrito):
                    print("Los campos no deben estar vacíos, complete los campos nuevamente.")
                    continue




        return [tipo_via, nombre_via, tipo_zona, nombre_zona, referencia, departamento, provincia, distrito]

def Fundamentación_del_pedido():
    while True:
        print("\nV. FUNDAMENTACIÓN DEL PEDIDO")
        fundamentacion=input()

        if not fundamentacion:
            print("El campo no puede estar vacío")
            continue

        return fundamentacion

def Documentos_adjuntados():
    while True:
        print("\nVI. DOCUMENTOS QUE SE ADJUNTAN")
        documentos_adjuntados=input()
        if not documentos_adjuntados:
            print("El campo no puede estar vacío")
            continue

        return documentos_adjuntados

def Fecha():
    fecha=datetime.datetime.now().strftime("%d/%m/%Y")
    return fecha


def Mostrar_trámite(codigo,resumen_pedido,autoridad,datos_personales,datos_direccion,fundamentacion_pedido,documentos_adjuntados,fecha):
    print("------DATOS REGISTRADOS DEL TRÁMITE------")
    print(f"\nCodigo:{codigo}")
    print("\nI. RESUMEN DE SU PEDIDO")
    print(resumen_pedido)

    print("\nII. DEPENDENCIA O AUTORIDAD A LA QUE SE DIRIGE")
    print(autoridad)

    print("\nIII. DATOS DEL SOLICITANTE")
    if len(datos_personales) == 7:
        print("Tipo de persona :", datos_personales[0])
        print("Apellido paterno:", datos_personales[1])
        print("Apellido materno:", datos_personales[2])
        print("Nombres         :", datos_personales[3])
        print("Documento       :", datos_personales[4])
        print("Correo          :", datos_personales[5])
        print("Teléfono        :", datos_personales[6])
    elif len(datos_personales) == 5:
        print("Tipo de persona :", datos_personales[0])
        print("Razón social    :", datos_personales[1])
        print("Documento       :", datos_personales[2])
        print("Correo          :", datos_personales[3])
        print("Teléfono        :", datos_personales[4])



    print("\nIV. DIRECCIÓN")
    print("Tipo de vía     :", datos_direccion[0])
    print("Nombre de vía  :", datos_direccion[1])
    print("Tipo de zona    :", datos_direccion[2])
    print("Nombre de zona  :", datos_direccion[3])
    print("Referencia      :", datos_direccion[4])
    print("Departamento    :", datos_direccion[5])
    print("Provincia       :", datos_direccion[6])
    print("Distrito        :", datos_direccion[7])

    print("\nV. FUNDAMENTACIÓN DEL PEDIDO")
    print(fundamentacion_pedido)

    print("\nVI. DOCUMENTOS QUE SE ADJUNTAN")
    print(documentos_adjuntados)

    print(f"\nFecha: {fecha}")
    print(f"\nEstado: Enviado")


def Formulario_Unico_de_Trámite():
    print("------FORMULARIO ÚNICO DE TRÁMITE------")
    i=Resumen_del_pedido()
    ii=Autoridad_a_la_que_se_dirige()
    iii=Datos_del_solicitante()
    iv=Direccion()
    v=Fundamentación_del_pedido()
    vi=Documentos_adjuntados()
    f=Fecha()
    tramite=[i,ii,iii,iv,v,vi,f]
    

    return tramite