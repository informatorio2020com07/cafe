def agregar_cafetera(cafeteria):
	print("Agregar Cafetera".center(centrado, "-"))
	capacidad = int(input("Capacidad de la nueva cafetera: "))
	cantidad = int(input("Cantidad actual en la nueva cafetera: "))
	nombre = input("nombre cafetera: ")

	cafetera = cafe.Cafetera(capacidad, cantidad, nombre)
	cafeteria.agregar_cafetera(cafetera)