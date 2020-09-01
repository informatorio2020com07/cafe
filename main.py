from cafe import Cafetera
from cafe import Cafeteria
import sys
import os
import mysql.connector

"""conexion con la base de datos"""
con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cafeteria"
        )
cursor=con.cursor()

def controlar_numero(valor):
    if valor.isdigit():
        return int(valor)
    else:
        return False

def cargar_base_datos():
    """carga la lista de cafe"""
    query="SELECT nombre_id,marca,modelo,id_tipo,capacidad, cantidad,funcionando FROM cafetera"
    cursor.execute(query)
    cafeteria1=Cafeteria("Cafecito007")
    for registro in cursor:
        cafetera=Cafetera(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6])
        cafeteria1.agregar_cafetera(cafetera)
    query="SELECT * FROM tipo_de_cafe"
    cursor.execute(query)
    lista_tipo=cursor.fetchall()
    return cafeteria1,lista_tipo


def listar_cafetera(cafeteria, lista_tipo):
    listar_cafetera=cafeteria.get_lista_cafetera()
    """ va a imprimir una lista de todas las cafeteras"""
    for index,cafetera in enumerate(listar_cafetera):
        mostrar=cafetera.to_dict()
        print("-----------")
        print(index+1,".-")
        for x in mostrar:
            if x == "tipoCafe":
                    
                print("     ",x,":",lista_tipo[mostrar[x]-1][1])
            else:
                print("     ",x,":",mostrar[x])


def listar_tipo_cafe(cafeteria, lista_tipo):
    """listar tipos de cafe"""
    for x,tipo in enumerate(lista_tipo):
        print(x+1,".-")
        print("Nombre:",tipo[1])
        print("Descripción:",tipo[2])
        print("")



def guardar_base_datos(cafetera):
    """guarda la nuevas cafetera DB"""
    query="""INSERT INTO cafetera(nombre_id,marca,modelo,Id_tipo,capacidad,
    cantidad,funcionando) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    datos=(cafetera.get_nombre(),cafetera.get_marca(),cafetera.get_modelo(),cafetera.get_tipo_de_cafe(),cafetera.get_capacidad(),cafetera.get_contenido(),cafetera.get_funcionando())
    cursor.execute(query,datos)
    con.commit()


def agregar_cafetera(cafeteria,lista_tipo):
    """Carga de datos"""
    print("Carga Cafetera: ")
    nombre = input("Ingrese el Nombre de la cafetera: ")
    print("")
    marca = input("Ingrese el Marca de la cafetera: ")
    print("")
    modelo = input("Ingrese el Modelo(año) de la cafetera: ")
    if modelo.isdigit():
        print("")
        print("Tipos de Cafe:")
        for y,x in enumerate(lista_tipo):
            print(x[1],end=" |")
        print("")
        print("Que cafe desea tomar 1 -",len(lista_tipo),": ",end="")
        tipo_de_cafe=input()
        tipo_de_cafe=controlar_numero(tipo_de_cafe)
        if tipo_de_cafe:
            if tipo_de_cafe<len(lista_tipo):
                print("")
                capacidad =input("Ingrese el Capacidad de la cafetera: ")
                print("")
                capacidad=controlar_numero(capacidad)
                if capacidad:
                    cant =input("Ingrese el Cantidad de la cafetera: ")
                    print("")
                    cant=controlar_numero(cant)
                    if cant:
                        if cant<capacidad:
                            print("Cafetara que esten 'funcionando' o 'descompuesta'")
                            funcionando = input("Ingrese el estado de la cafetera: ")
                            if funcionando=="funcionando" or funcionando=="descompuesta":
                                """Creamos el objeto cafetera y lo agregamos a la lista siempre que el nombre no se repita"""
                                cafetera=Cafetera(nombre,marca,modelo,tipo_de_cafe,capacidad,cant,funcionando)
                                try:
                                    cafeteria.agregar_cafetera(cafetera)
                                    guardar_base_datos(cafetera)
                                    print("Guardado con exito")
                                except Exception as ex:
                                    print(ex)


def modificar_base_datos(cafetera):
    """modifica la cafetera DB
    usar en usar cafetera estado y servir"""
    query="""UPDATE cafetera set nombre_id=%s,marca=%s,modelo=%s,Id_tipo=%s,
    capacidad=%s,cantidad=%s,funcionando=%s where nombre_id=%s"""
    datos=(cafetera.get_nombre(),cafetera.get_marca(),cafetera.get_modelo(),cafetera.get_tipo_de_cafe(),cafetera.get_capacidad(),cafetera.get_contenido(),cafetera.get_funcionando(),cafetera.get_nombre())
    cursor.execute(query,datos)
    con.commit()



def usar_cafetera(cafeteria,lista_tipo):
    estado_cafetera(cafeteria, lista_tipo)
    Elige=input("Nombre de cafetera: ")
    cafetera=cafeteria.buscar_cafetera_por_nombre(Elige)
    if cafetera:
        print("""
            1 - Llenar
            2 - Vaciar
            3 - Recargar
            4 - cambiar estado
            5 - quitar cafetera
            """)

        elegido=input("Ingrese la opción deseada: ")
        try:
            if elegido=="1":
                cafetera.llenar_cafetera()
                print("cafetera llena")
            elif elegido=="2":
                cafetera.vaciar_cafetera()
                print("cafetera vacia")
            elif elegido=="3":
                cantidad=input("Ingrese cuanto desea recargar: ")
                cantidad=controlar_numero(cantidad)
                if cantidad:
                    cafetera.recargar(cantidad)
                    print("cafetera recargada")
            elif elegido=="4":
                estado=input("Cual es el estado de la cafetera: 'funcionando' o 'descompuesta': ")
                cafetera.set_estado(estado.lower())
                print("cafetera ",cafetera.get_nombre(),"esta ",estado)
            elif elegido=="5":
                cafeteria.quitar_cafetera_nombre(cafetera.get_nombre())
                print("cafetera llena",cafetera.get_nombre(),"Borrada")
            modificar_base_datos(cafetera)
        except Exception as ex:
            print(ex)
    else:
        print("Nombre de la cafetera incorrecto")

def servir_cafe(cafeteria,lista_tipo):
    listar_tipo_cafe(cafeteria, lista_tipo)
    cafeteria_aux=Cafeteria("Auxiliar")
    print("Que cafe desea tomar 1 -",len(lista_tipo),": ",end="")
    tipo=input()
    tipo=controlar_numero(tipo)
    if tipo:
        lista_cafetera=cafeteria.get_lista_cafetera()
        for x in lista_cafetera:
            if x.get_tipo_de_cafe()== tipo and x.get_estado():
                cafeteria_aux.agregar_cafetera(x)
        print("""
            1 - Chico        100cc
            2 - Medio        200cc
            3 - Medio Grande 250cc
            4 - Grande       300cc
            """)
        opc= {"1":100,
            "2":200,
            "3":250,
            "4":300 }
        tamaño=input("Ingrese número: ")
        cuanto=input("Cuantas tazas:")
        cuanto=controlar_numero(cuanto)
        if cuanto and tamaño in opc:
            while cuanto>0 and len(cafeteria.get_lista_cafetera())>0:
                estado_cafetera(cafeteria_aux, lista_tipo)
                usar=input("Ingrese el nombre de la cafetera que desea usar: ")
                cafetera=cafeteria_aux.buscar_cafetera_por_nombre(usar)
                if cafetera:    
                    taza=cafetera.cuantas_tazas(opc.get(tamaño))
                    if cuanto<=taza:
                        tenia=cafetera.get_contenido()
                        cafetera.servir(cuanto*opc.get(tamaño))
                        cuanto=0
                        print(cafetera.get_nombre()," tenia ",tenia,"cc que con ",cafetera.get_contenido(),"cc")
                        print("Disfrute su cafe")
                    else:
                        cafetera.servir(taza*opc.get(tamaño))
                        cuanto=cuanto-taza
                        print(cafetera.get_nombre()," solo puede servir ",taza," tazas")
                        print("faltaron servir ",cuanto," tazas")
                        if len(cafeteria_aux.get_lista_cafetera())==1:
                            print("No hay mas de ese tipo de cafe")
                            cuanto=0
                    modificar_base_datos(cafetera)
 

def estado_cafetera(cafeteria,lista_tipo):
    lista_cafetera=cafeteria.get_lista_cafetera()
    
    lista_estado=[]
    for cafetera in lista_cafetera:
        estado_cafet=[]
        estado_cafet.append(cafetera.get_nombre())
        estado_cafet.append(cafetera.get_marca())
        estado_cafet.append(cafetera.get_capacidad())
        estado_cafet.append(cafetera.get_contenido())
        if cafetera.get_estado():
            estado_cafet.append("funcionando")
        else:
            estado_cafet.append("descompuesta")
        lista_estado.append(estado_cafet)

    tabla="""\
+-------------------------------------------------------+
| cafetera    marca     capacidad contenido   estado    |
|-------------------------------------------------------|
{}
+-------------------------------------------------------+\
"""
    tabla=tabla.format('\n'.join("| {:<9} {:<10} {:>10} {:>8} {:>12} |".format(*fila)
        for fila in lista_estado))
    print(tabla)


def borrar_base_datos(cafetera):
    """borrar la cafetera de DB"""
    query="DELETE FROM cafetera where nombre_id=%s"
    dato=(cafetera.get_nombre(),)
    cursor.execute(query,dato)
    con.commit()


def quitar_cafetera(cafeteria,lista_tipo):
    """borra la cafetera de la lista"""
    listar_cafetera(cafeteria,lista_tipo)
    print("")
    print("Quitar cafetera".center(20, "-"))
    print("")
    borrar=input("Que cafetera desea borrar ingrese numero: ")
    borrar=controlar_numero(borrar)
    if borrar and borrar <= cafeteria.get_cantidad_cafeteras():
        cafetera_borrar=cafeteria.get_lista_cafetera()[borrar -1]
        if cafeteria.quitar_cafetera_nombre(cafetera_borrar.get_nombre()):
            print("Cafetera borrada")
            print(" ",cafetera_borrar.get_nombre(),cafetera_borrar.str_cant_sobre_capacidad())
            borrar_base_datos(cafetera_borrar)
    else:
        print("No existe ese numero de cafetera")

        
def salir(cafeteria,lista_tipo):
    cursor.close()
    con.close()
    sys.exit(0)

    
def menu_pantalla(opciones):    
#imprime en pantalla cualquier menu de opciones siempre que se ingrese la lista o tupla de opciones correspondientes
    os.system("Cls") 
    print("""
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    print(opciones[0].center(64,"-"))
    print(" ")
    print(opciones[1])
    

def menu_principal(cafeteria, lista_tipo):
 
    menuPrincipal_opciones = ("Administración de cafeteras", """
    1- Listar Cafeteras
    2- Listar Tipo de Cafe
    3- Agregar Cafetera
    4- Quitar Cafetera
    5- Usar Cafetera
    6- Estado de Cafetera
    7- Servir café
    8- Salir
    """)

    opciones = {"1" : listar_cafetera,
        "2" : listar_tipo_cafe,
        "3" : agregar_cafetera,
        "4" : quitar_cafetera, 
        "5" : usar_cafetera, 
        "6" : estado_cafetera, 
        "7" : servir_cafe, 
        "8" : salir }

    while True:
        menu_pantalla(menuPrincipal_opciones)
        opcion = input("elige una opción: ")
        accion = opciones.get(opcion)
        if accion:
            accion(cafeteria, lista_tipo)
        else:
            print("{0} no es una opción válida".format(opcion))
        print("")
        input("Volver al menu")
    
def main():
    
    cafeteria, lista_tipo=cargar_base_datos()
    #carga las cafeteras de la base de dato
    menu_principal(cafeteria, lista_tipo)


if __name__ == "__main__":
    main()