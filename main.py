from cafe import Cafetera
from cafe import Cafeteria
import sys
import os
import mysql.connector
def cargar_base_datos():
    """carga la lista de cafe"""
    conexion1=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cafeteria"
        )
    cursor=conexion1.cursor()

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

def listar_cafetera(lista_cafetera):
    """ va a imprimir una lista de todas las cafeteras"""
    for index,cafetera in enumerate(lista_cafetera):
        mostrar=cafetera.to_dict()
        print("-----------")
            print(index+1,".-")
            for x in mostrar:
                print(x,":",motrar[x])

def guardar_base_datos(cafetera):
    """guarda la nuevas cafetera DB"""
    query1="""INSERT INTO cafetera(nombre_id,marca,modelo,Id_tipo,capacidad,
    cantidad,funcionando) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    datos=(cafetera.get_nombre(),cafetera.get_marca(),cafetera.get_modelo(),cafetera.get_tipo_de_cafe(),cafetera.get_capacidad(),cafetera.get_contenido(),cafetera.get_funcionando())
    cursor.execute(query,datos)

def agregar_cafetera(lista_tipo):
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
        print(x,end=" ")
    tipo_de_cafe = input("Ingrese el Tipo de Cafe de la cafetera: ")
    """cambia el tipo cafe por su indice"""
    for index,x in lista_tipo:
        if tipo_de_cafe.lower()==x.lower():
            tipo_de_cafe=index+1
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
    except Exception as ex:
        print(ex)
        
def modificar_base_datos(cafetera):
    """modifica la cafetera DB
    usar en usar cafetera estado y servir"""
    query="""UPDATE cafetera set nombre_id=%s,marca=%s,modelo=%s,Id_tipo=%s,
    capacidad=%s,cant=%s,funcionando=%s where nombre=%s"""
    datos=(cafetera.get_nombre(),cafetera.get_marca(),cafetera.get_modelo(),cafetera.get_tipo_de_cafe(),cafetera.get_capacidad(),cafetera.get_contenido(),cafetera.get_funcionando(),cafetera.get_nombre())
    cursor.execute(query,datos)

def usar_cafetera():
    pass
        
def estado_cafetera():
    pass
    
def servir_cafe():
    pass





def borrar_base_datos(cafetera):
    """borrar la cafetera de DB"""
    query="DELETE FROM cafetera where nombre_id=%s"
    dato=cafetera.get_nombre()
    cursor.execute(query,dato)

def quitar_cafetera(cafeteria):
    print("Quitar cafetera".center(20, "-"))
    print("")
    listar_cafeteras(cafeteria.get_lista_cafetera())
    borrar=int(input("Que cafetera desea borrar ingrese numero: "))
    if borrar >= cafeteria.get_cantidad_cafeteras()
        cafetera_borrar=cafeteria.get_lista_cafetera()[borrar -1]
        if cafeteria.quitar_cafetera(cafetera_borrar):
            print("Cafetera borrada")
            print(" ",cafetera_borrar.get_nombre(),cafetera_borrar.str_cant_sobre_capacidad())
            borrar_base_datos(cafetera_borrar)
    else:
        print("No existe numero de cafetera")


        
def salir(cafeteria):
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
    2- Agregar Cafetera
    3- Quitar Cafetera
    4- Usar Cafetera
    5- Estado de Cafetera
    6- Servir café
    7- Salir
    """)
    opciones = {"1" : listar_cafetera, 
        "2" : agregar_cafetera, 
        "3" : quitar_cafetera, 
        "4" : usar_cafetera, 
        "5" : estado_cafetera, 
        "6" : servir_cafe, 
        "7" : salir }
    while True:
        menu_pantalla(menuPrincipal_opciones)
        opcion = input("elige una opción: ")
        accion = opciones.get(opcion)
        print(accion)
        if accion:
            accion(cafeteria)
        else:
            print("{0} no es una opción válida".format(opcion))

    
    
def main():
    
    #cafeteria = iniciar_cafeteria() #¿?no he visto la función aún
    menu_principal()


if __name__ == "__main__":
    main()