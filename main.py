from cafe import Cafetera
from cafe import Cafeteria
import sys
import os
import mysql.connector
def cargar_base_datos():
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

def quitar_cafetera(cafeteria):
    print("Quitar cafetera".center(20, "-"))
    print("")
    listar_cafeteras()
    borrar=int(input("Que cafetera desea borrar: "))
    """cafetera=cafeteria.get_cafeteras()
    mostrar_cafeteras_enumeradas(cafeteras)
    
    cafetera_borrar=cafeteras[borrar -1]
    cafeteria.quitar_cafetera(cafetera_borrar)
    input()
    print(" ",cafetera_borrar.get_nombre(),cafetera_borrar.str_cant_sobre_capacidad())"""

def listar_cafetera(lista_cafetera):
    """ va a imprimir una lista de todas las cafeteras"""
    for cafetera in lista_cafetera:
        mostrar=cafetera.to_dict()
        print("-----------")
        for x in mostrar:
            print(x,":",motrar[x])

def agregar_cafetera(lista_tipo):
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
    print("")
    capacidad = input("Ingrese la Capacidad de la cafetera: ")
    print("")
    cant = input("Ingrese la Cantidad de café de la cafetera: ")
    print("")
    print("ingrese el estado de la cafetera funcionando - no funcionando")
    funcionando = input("Ingrese el estado de la cafetera: ")

    cafetera=Cafetera(nombre,marca,modelo,tipo_de_cafe,capacidad, cant,funcionando)
    cafeteria.agregar_cafetera(cafetera)

def usar_cafetera(cafeteria):
    cafetera = cafeteria.get_lista_cafetera()
    print("Opciones de cafeteras: ", cafetera)
	
	#elegir cafetera
    cafetera_seleccion = int(input("Qué cafetera usar: "))
    cafetera_seleccionada = cafetera[cafetera_seleccion]

    opcion = 0
    while opcion not in (1,2,3,4):
        print("1- servir cafe")
        print("2- recargar cafe")
        print("3- llenar cafetera")
        print("4- vaciar cafetera")
        opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        #servir café eligiendo cafetera
        opcion1=True
        while opcion1:
            print("Desea operar en: ")
            print("1- Taza")
            print("2- CC")
            opcion1=int(input("Ingrese opción: "))
            if opcion1==1:
                tamaño=int(input("Tamaño de taza: "))
                cantidad_tazas=cafetera_seleccionada.cuantas_tazas(tamaño)
                print("puede servir", cantidad_tazas)
                servir_taza=int(input("Cuántas tazas: "))
                try:
                    cafetera_seleccionada.servir(tamaño*servir_taza)
                    break
                except ValueError as ex:
                    print(ex)
                    opcion1=True
            elif opcion1==2:
                cc=int(input("Cuántos cc: "))
                try:
                    cafetera_seleccionada.servir(cc)
                    break
                except ValueError as ex:
                    print(ex)
                    opcion1=True
            else:
                print("No es una opción posible")
                opcion1=True

    elif opcion == 2:
        #recargar cafe
        print(cafetera_seleccionada.str_cant_sobre_capacidad())
        cant_cafe_recargar=int(input("Cuántos cc de café desea recargar: "))
        try:
            cafetera_seleccionada.recargar(cant_cafe_recargar)
        except ValueError as error:
            print(error)
    elif opcion == 3:
        cafetera_seleccionada.llenar_cafetera()
    else:
        cafetera_seleccionada.vaciar_cafetera()
        
def estado_cafetera():
    pass
    
def servir_cafe():
    pass
        
def salir():
    
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