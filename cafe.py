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

    def get_admisible(self):
        #Retorna cuanto le falta a una cafetera para alcanzar su capacidad.
        return self.__capacidad - self.__cant  
    
    def esta_vacia(self):
        #Retorna True si la cafetera no tiene cafe, caso contrario retorna False
        if self.__capacidad == self.get_admisible():
            return True
        else:
            return False

    def esta_llena(self):
        #Si el elemento cafetera esta llena cap=cant devuelve true, sino devuelve false
        if self.__capacidad == self.__cant:
            return True
        else:
            return False            

    def llenar_cafetera(self):
        self.__cant = self.__capacidad

    def recargar(self, cantidad):
    #metodo para recargar una cafetera, recibe la cantidad a recargar. Si se pasa dev. un error.
        if self.__cant + cantidad <= self.__capacidad:
            self.__cant += cantidad
        else:
            raise ValueError("No hay suficiente capacidad para recargar esa cantidad")

    def vaciar_cafetera(self):
        self.__cant=0   

    def str_cant_sobre_capacidad(self):
        cadena = str(self.__cant) + "/" + str(self.__capacidad)
        return cadena

class Cafeteria:
    def __init__(self, nombre):
			self.__lista_cafeteras = []
			self.__nombre = nombre

    def get_cantidad_cafeteras(self):
        return len(self.__lista_cafeteras)


if __name__ == "__main__":
    pass