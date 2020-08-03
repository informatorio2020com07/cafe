import cafe

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

if __name__ == "__main__":
    main()