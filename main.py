import cafe
import sys
import os
import mysql.connector
conexion1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cafeteria"
    )
cursor=conexion1.cursor()

query="SELECT * FROM cafeteria"
cursor.execute(query)
cafeteria=Cafeteria("Cafecito007")
for registro in cursor:
    cafetera=Cafetera(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7])   
    cafeteria.agregar_cafetera(cafetera)
query="SELECT * FROM tipo_de_cafe"
cursor.execute(query)
lista_tipo=cursor.fetchall()


def quitar_cafetera(cafeteria):
    print("Quitar cafetera".center(centrado, "-"))
    print("")
    cafetera=cafeteria.get_cafeteras()
    mostrar_cafeteras_enumeradas(cafeteras)
    borrar=int(input("Que cafetera desea borrar: "))
    cafetera_borrar=cafeteras[borrar -1]
    cafeteria.quitar_cafetera(cafetera_borrar)
    input()
    print(" ",cafetera_borrar.get_nombre(),cafetera_borrar.str_cant_sobre_capacidad())

def listar_cafetera():
    pass

def agregar_cafetera():
    pass
    
def usar_cafetera():
    pass
        
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
        if accion:
            accion()
        else:
            print("{0} no es una opción válida".format(opcion))

    
    
def main():
    pass
    #cafeteria = iniciar_cafeteria() #¿?no he visto la función aún
    menu_principal()


if __name__ == "__main__":
    main()