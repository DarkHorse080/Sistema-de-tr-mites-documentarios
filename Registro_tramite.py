from Formulario_Trámite import Mostrar_trámite
from Operaciones import convertir_a_lista,convertir_a_texto
from pathlib import Path

def Registrar_Tramite(tramite):
    tramite_completo=[]
    posicion=0
    ruta = Path("Trámites.txt")
    codigo=None
    if not ruta.exists():
        with open(ruta, "w", encoding="utf-8") as tramites:
            pass

    with open(ruta, "r", encoding="utf-8") as tramites:
                lineas = tramites.readlines()
                if lineas:  
                    ultima_linea = convertir_a_lista(lineas[-1])
                    nuevo_codigo=f"TR-00{int(ultima_linea[0][5:])+1}"
                    tramite_completo.append(nuevo_codigo)
                else:
                    nuevo_codigo="TR-001"
                    tramite_completo.append(nuevo_codigo)
        

    
    for i in tramite:
        if posicion==2:
            for j in i:
                tramite_completo.append(j)
        elif posicion==3:
            for k in i:
                tramite_completo.append(k)
        else:
            tramite_completo.append(i)

        posicion+=1

    estado="Enviado"
    tramite_completo.append(estado)
    if lineas:
        tramite_a_registrar="\n"+convertir_a_texto(tramite_completo.copy())
    else:
        tramite_a_registrar=convertir_a_texto(tramite_completo.copy())


    with open(ruta, "a", encoding="utf-8") as tramites:
        tramites.write(tramite_a_registrar)

    Mostrar_trámite(nuevo_codigo,tramite[0],tramite[1],tramite[2],tramite[3],tramite[4],tramite[5],tramite[6])
    
    print("Trámite Registrado Correctamente")

    


