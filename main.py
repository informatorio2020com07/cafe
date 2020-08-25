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
    for tipo in lista_tipo:
        print("Nombre:",tipo[1])
        print("Descripción:",tipo[2])

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
    modelo = input("Ingrese el Modelo de la cafetera: ")
    print("")
    print("Tipos de Cafe:")
    for x in lista_tipo:
        print(x[1],end=" |")
    print("")
    tipo_de_cafe = input("Ingrese el Tipo de Cafe de la cafetera: ")
    """cambia el tipo cafe por su indice"""
    for index,x in enumerate(lista_tipo):
        if tipo_de_cafe.lower()==x[1].lower():
            tipo_de_cafe=index+1
            break
    print("")
    capacidad = input("Ingrese el Capacidad de la cafetera: ")
    print("")
    cant = input("Ingrese el Cantidad de la cafetera: ")
    print("")
    print("ingrese el estado de la cafetera funcionando - no funcionando")
    funcionando = input("Ingrese el estado de la cafetera: ")
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
    capacidad=%s,cant=%s,funcionando=%s where nombre=%s"""
    datos=(cafetera.get_nombre(),cafetera.get_marca(),cafetera.get_modelo(),cafetera.get_tipo_de_cafe(),cafetera.get_capacidad(),cafetera.get_contenido(),cafetera.get_funcionando(),cafetera.get_nombre())
    cursor.execute(query,datos)
    con.commit()



def usar_cafetera(cafeteria,lista_tipo):
    pass
      

def estado_cafetera(cafeteria,lista_tipo):
    pass
   

def servir_cafe(cafeteria,lista_tipo):
    pass


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
    borrar=int(input("Que cafetera desea borrar ingrese numero: "))
    if borrar <= cafeteria.get_cantidad_cafeteras():
        cafetera_borrar=cafeteria.get_lista_cafetera()[borrar -1]
        if cafeteria.quitar_cafetera_nombre(cafetera_borrar.get_nombre()):
            print("Cafetera borrada")
            print(" ",cafetera_borrar.get_nombre(),cafetera_borrar.str_cant_sobre_capacidad())
            borrar_base_datos(cafetera_borrar)
    else:
        print("No existe ese numero de cafetera")

        
def salir(cafeteria):
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
    
        
def menu_principal():
    #carga las cafeteras de la base de dato
    cafeteria,lista_tipo=cargar_base_datos()
    
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
        print(accion)
        if accion:
            accion(cafeteria, lista_tipo)
        else:
            print("{0} no es una opción válida".format(opcion))
        a=input("")

    
    
def main():
    
    #cafeteria = iniciar_cafeteria() #¿?no he visto la función aún
    menu_principal()


if __name__ == "__main__":
    main()