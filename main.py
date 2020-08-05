import cafe
import mysql.connector
def BaseDato():
        conexion1=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="cafeteria",auth_plugin="mysql_native_password")
        basedato=conexion1.cursor()


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

def main():
    pass
    1>2 3<4 4<2 5<3

if __name__ == "__main__":
    main()