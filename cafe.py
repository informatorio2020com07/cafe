class Cafetera:

    def __init__(self, capacidad, cant, marca, modelo, nombre_id):
        self.__capacidad = capacidad
        self.__cant = cant
        self.__marca = marca
        self.__modelo = modelo
        self.__nombre_id = nombre_id


    def get_capacidad(self):
    	return self.__capacidad

    def get_contenido(self):
        return self.__cant

    def llenar_cafetera(self):
        self.__cant = self.__capacidad

    def recargar(self, cantidad):
    #metodo para recargar una cafetera, recibe la cantidad a recargar. Si se pasa dev. un error.
        if self.__cant + cantidad <= self.__capacidad:
            self.__cant += cantidad
        else:
            raise ValueError("No hay suficiente capacidad para recargar esa cantidad")      

class Cafeteria:
    def __init__(self, nombre):
			self.__lista_cafeteras = []
			self.__nombre = nombre

    def get_cantidad_cafeteras(self):
        return len(self.__lista_cafeteras)


if __name__ == "__main__":
    pass