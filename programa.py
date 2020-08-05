import cafe04
import os

#Ver Cafeteras 	
#listar cafeteras
#Agregar/quitar Cafetera #agregar nueva cafetera #borrar cafetera
#Usar Cafetera
	#elegir cafetera
		#llenar cafetera
		#vaciar cafetera
		#servir cafe
		#recargar cafe
#Salir

#para centrar los textos con un mismo valor.
centrado = 60

def iniciar_cafeteria():
	#iniciar una cafeteria con datos de prueba
	cafeteria = cafe04.Cafeteria("LA VIELA")

	caf1 = cafe04.Cafetera(2500, 500, "CAFETERA01")
	cafeteria.agregar_cafetera(caf1)

	caf2 = cafe04.Cafetera(1500, 1000, "CAFETERA02")
	cafeteria.agregar_cafetera(caf2)

	caf3 = cafe04.Cafetera(1000, 0, "CAFETERA03")
	cafeteria.agregar_cafetera(caf3)

	caf4 = cafe04.Cafetera(3000, 0, "CAFETERA04")
	cafeteria.agregar_cafetera(caf4)

	return cafeteria	


def imprimir_encabezados(cadena):
	os.system("cls")
	print()
	print(cadena.center(centrado,"-"))
	print()


def imprimir_menu_principal():
	#imprimir menu principal
	imprimir_encabezados("Cafe Admin V.04")
	print("	1- Listar Cafeteras")
	print("	2- Agregar Cafetera")
	print("	3- Quitar Cafetera")
	print("	4- Usar Cafetera")
	print("	5- Estado de la Cafetría")
	print("	6- Listar cafeteras como diccionarios")
	print("	7- Servir pasando nombre de cafetera y cantidad")
	print("	8- Salir")
	print()

def listar_cafeteras(lista_cafeteras):
	#listar cafeteras
	imprimir_encabezados("CA-Listar cafeteras")
	for x in lista_cafeteras:
		print(" Nombre cafetera: ", x.get_nombre())
		print(" Capacidad: ", x.get_capacidad())
		print(" Cantidad : ", x.get_cantidad())
		print(" Cant/Capac.:",x.str_cant_sobre_capacidad())
		print("-"*30)
	a =	input("Seguir ...")

def agregar_cafetera(cafeteria):
	#agregar cafetera en una cafeteria
	imprimir_encabezados("CA-Agregar Cafetera")
	capacidad = int(input(" Capacidad de la nueva cafetera: "))
	cantidad = int(input(" Cantidad actual en la nueva cafetera: "))
	siempre = True
	while siempre:
		if cantidad <= capacidad:
			siempre = False
		else:
			a = input("...capacidad menor que cantidad...ingrese correctamente los datos!!!!")
			os.system("cls")
			print("CA-Agregar Cafetera".center(centrado, "-"))
			print(" ")
			capacidad = int(input(" Capacidad de la nueva cafetera: "))
			cantidad = int(input(" Cantidad actual en la nueva cafetera: "))		
	nombre = input(" Nombre cafetera: ")
	cafetera = cafe04.Cafetera(capacidad, cantidad, nombre)
	cafeteria.agregar_cafetera(cafetera)

def mostrar_cafeteras_enumeradas(lista_cafeteras):
	#listar cafeteras enumeradas
	for indice, cafetera in enumerate(lista_cafeteras):
		print(indice+1, cafetera.get_nombre(), cafetera.str_cant_sobre_capacidad())

def quitar_cafetera(cafeteria):
	#quitar cafetera de una cafeteria
	imprimir_encabezados("CA-Quitar Cafetera")
	cafeteras = cafeteria.get_cafeteras()
	mostrar_cafeteras_enumeradas(cafeteras)
	#cual_borrar = int(input("Que Cafetera borrar 1: "))
	#cual_borrar -= 1
	cual_borrar = - 2
	siempre = True
	while siempre:
		
		if len(cafeteras) == 0:
			a = input(" no hay cafetas para borrar") 
			siempre = False
		
		elif 0 <= int(cual_borrar) < int(len(cafeteras)):
			cafetera_borrar = cafeteras[cual_borrar]
			cafeteria.quitar_cafetera(cafetera_borrar)
			print(" ")
			print(" ", cafetera_borrar.get_nombre(), cafetera_borrar.str_cant_sobre_capacidad())
			print("  quitada.")
			a = input("Seguir...")
			siempre = False
		
		else:	
			print(" debe ingresar un numero dentro del rango enumerado...")
			cual_borrar = int(input("Que Cafetera borrar: "))
			cual_borrar -= 1
			siempre = True	

def usar_cafetera(cafeteria):
	#seleccionar una cafetera, y elegir el uso.
	cafeteras = cafeteria.get_cafeteras()
	mostrar_cafeteras_enumeradas(cafeteras)
	#elegir cafetera
	cafetera_seleccion = int(input("Que cafetera usar: "))
	cafetera_seleccionada = cafeteras[cafetera_seleccion-1]

	opcion = 0
	while opcion not in (1,2,3,4):
		os.system("cls")
		print("Usar cafetera {}".format(cafetera_seleccionada.get_nombre()).center(centrado,"-"))
		print(" ")
		print(" 1- servir cafe")
		print(" 2- recargar cafe")
		print(" 3- llenar cafetera")
		print(" 4- vaciar cafetera")
		opcion = int(input(" Ingrese una opción: "))

	if opcion == 1:
		#TODO
		#servir cafe
		siempre = True
		while siempre:
			print("Desea operar en:")
			print("1- Taza")
			print("2- CC")
			print("3_ Salir a menu anterior")
			opcion1=int(input("Ingrese opción: "))
			if  opcion1 == 1:
				tamaño=int(input("Tamaño de taza: "))
				cantidad_tazas=cafetera_seleccionada.cuantas_tazas(tamaño)
				print("puede servir",cantidad_tazas)
				servir_taza=int(input("cuántas tazas: "))
				try:
					cafetera_seleccionada.servir(tamaño*servir_taza)
					#break
				except ValueError as ex:
					print(ex)
					siempre=True
			elif opcion1 == 2:
				cc=int(input("Cuántos CC: "))
				try:
					cafetera_seleccionada.servir(cc)
					#break
				except ValueError as ex:
					print(ex)	
					siempre = True
			else:
				print("No es una opción posible")
				siempre = False	


	elif opcion == 2:
		os.system("cls")
		print(" ")
		print("CA-UC-Recargar cafetera".center(centrado,"-"))		
		maximo = cafetera_seleccionada.get_admisible()
		print(" ")
		print("A {} \npuede recargarle {} cc.".format(cafetera_seleccionada.get_nombre(),maximo))
		print(" ")
		cantidad_a_recargar = int(input("Cntidad a recargar :"))
		
		try:
			cafetera_seleccionada.recargar(cantidad_a_recargar)
		
		except ValueError as er:
			print(er)
		
	elif opcion == 3:

		cafetera_seleccionada.llenar_cafetera()
		print("{} ahora está llena". format(cafetera_seleccionada))
		a =	input("Seguir ...")
	else:
		cafetera_seleccionada.vaciar_cafetera()
		print("{} ahora está vacia". format(cafetera_seleccionada))
		a =	input("Seguir ...")

def estado_cafeteria(cafeteria):
	#Imprime informacion sobre el estado de la cafeteria respecto de las cafeteras
	imprimir_encabezados("CA-Estdo de la cafetería")
	print("La cafetería {} cunta con {} cafeteras.".
		format(cafeteria.get_nombre(),cafeteria.cuantas_cafeteras_hay()))
	
	print(" ")
	print("Cafeteras llenas :  {} ".format(cafeteria.cuantas_cafeteras_llenas()))
	print(" ")
	print("Cafeteras vacias :  {} ".format(cafeteria.cuantas_cafeteras_vacias()))
	print(" ")
	print("Cafeteras con contenido :  {} acumulan un total de {} cc. de café. ".
			format(cafeteria.cuantas_cafeteras_no_vacias(), cafeteria.cuanta_cantidad_de_cafe()))
	print("-"*70)
	a = input("seguir") 

def ver_dicc_cafeteras(cafeteria):
	#Muestra una lista de diccionarios con las cafeteras que hay en la cafeteria 
	print(" ")
	print("CA-Ver cafeteras como diccionarios".center(centrado,"-"))
	lstdicc = cafeteria.get_cafeteras_dict()
	for elem in lstdicc:
		print(elem)
	a = input("Estas son las cafeteras disponibles en {}. Seguir...".format(cafeteria.get_nombre())) 	

def servir_desde_cafeteria(cafeteria):
	imprimir_encabezados("CA-Servir pasando cafetera y cantidad")
	ver_dicc_cafeteras(cafeteria)
	print(" ")
	print("Considere Mayúsculas y Minusculas!!")
	nombre_cafetera = input("De qué cafetera querés servir? ingresá el nombre:") 
	while True:
		try:
			cantidad_servir = int(input("Cantidad a servir            : "))
			break
		except ValueError as e:
			print("Ingrese una cantidad válida...")

	cafeteria.servir_cafe(nombre_cafetera,cantidad_servir)
	ver_dicc_cafeteras(cafeteria)

def main():
	#Programa principal
	ejecutandose = True
	cafeteria = iniciar_cafeteria()

	while ejecutandose:
		opcion = 0
		while opcion not in (1,2,3,4,5,6,7,8):
			imprimir_menu_principal()
			opcion = int(input("Ingrese opción: "))
			print(" ")

		if   opcion == 1:
			#listar cafeteras
			listar_cafeteras(cafeteria.get_cafeteras())
		elif opcion == 2:
			#agregar/quitar cafeteras
			agregar_cafetera(cafeteria)
		elif opcion == 3:
			#agregar/quitar cafeteras
			quitar_cafetera(cafeteria)	
		elif opcion == 4:
			#Usar Cafetera
			usar_cafetera(cafeteria)
		elif opcion == 5:
			#Muestra el estado de las cafeterias usando varios metodos y funciones de la clase
			estado_cafeteria(cafeteria)
		elif opcion == 6:
			#Muestra lista de cafeteras como diccionario.
			ver_dicc_cafeteras(cafeteria)
		elif opcion == 7:
			#Servir desde cafeteria pasando nombre y cantidad.
			servir_desde_cafeteria(cafeteria)	
		else:
			ejecutandose = False

#ejecutando el programa principal
if __name__ == "__main__":
	main()