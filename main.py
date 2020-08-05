import cafe
import os

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
	
def menu_pantalla(opciones):	
#imprime en pantalla cualquier menu de opciones siempre que se ingrese la lista o tupla de opciones correspondientes
	os.system("Cls") 
	print(" ")
	print(opciones[0].center(64,"-"))
	print(" ")
	for i in range (1,len(opciones)):
		print(opciones[i])
		print(" ")	
		
def menu_principal():
	#imprime en pantalla el menú principal usando menu_pantalla y devuleve una opción válida
	menuPrincipal_opciones = ("Administración de cafeteras", " 1- Listar Cafeteras", " 2- Agregar Cafetera", " 3- Quitar Cafetera", " 4- Usar Cafetera", " 5- Estado de Cafetera", " 6- Servir café", " 7- Salir")
	
	menu_pantalla(menuPrincipal_opciones)
	opcion = input("Ingrese opción: ")
	print(" ")
	while opcion not in ("1","2","3","4","5","6","7"):		
		menu_pantalla(menuPrincipal_opciones)
		opcion = input("Ingrese opción: ")	
		print(" ")
	opcion = int(opcion)
	return opcion
	
def main():
	abierto = True
	#cafeteria = iniciar_cafeteria() #¿?no he visto la función aún
	while abierto:
		opcion=menu_principal()
		if   opcion == 1:
			#listar cafeteras
			pass
		elif opcion == 2:
			#agregar cafeteras
			pass
		elif opcion == 3:
			#quitar cafeteras
			try:
				quitar_cafetera(cafeteria)
			except:
				print("¡¡¡¡¡¡¡¡en construcción!!!!!!!!")
				input("seguir")
				pass
		elif opcion == 4:
			#Usar Cafetera
			pass
		elif opcion == 5:
			#Muestra el estado de las cafeterias usando varios metodos y funciones de la clase
			pass
		elif opcion == 6:
			#Servir desde cafeteria entrando nombre y cantidad.
			pass
		else:
			abierto = False

if __name__ == "__main__":
    main()