class Cafetera:

    def __init__(self, capacidad, cant, marca, modelo, nombre_id):
        self.__capacidad = capacidad
        self.__cant = cant
        self.__marca = marca
        self.__modelo = modelo
        self.nombre_id = nombre_id


    def get_capacidad(self):
    	return self.__capacidad

    def get_contenido(self):
        return self.__cant


class Cafeteria:
    pass

    def get_cantidad_cafeteras(self):
        return len(self.lista_cafeteras)


if __name__ == "__main__":
    pass