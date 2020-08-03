class Cafetera:

    def __init__(self, capacidad, cant, marca, modelo, nombre_id):
        self.__capacidad = capacidad
        self.__cant = cant
        self.__marca = marca
        self.__modelo = modelo
        self.__nombre_id = nombre_id

    def get_nombre(self):
        return self.__nombre_id

    def get_capacidad(self):
        return self.__capacidad

    def get_contenido(self):
        return self.__cant

    def get_admisible(self):
        # Retorna cuanto le falta a una cafetera para alcanzar su capacidad.
        return self.__capacidad - self.__cant

    def esta_vacia(self):
        # Retorna True si la cafetera no tiene cafe, caso contrario retorna False
        if self.__capacidad == self.get_admisible():
            return True
        else:
            return False

    def esta_llena(self):
        # Si el elemento cafetera esta llena cap=cant devuelve true, sino devuelve false
        if self.__capacidad == self.__cant:
            return True
        else:
            return False

    def llenar_cafetera(self):
        self.__cant = self.__capacidad

    def recargar(self, cantidad):
        # metodo para recargar una cafetera, recibe la cantidad a recargar. Si se pasa dev. un error.
        if self.__cant + cantidad <= self.__capacidad:
            self.__cant += cantidad
        else:
            raise ValueError(
                "No hay suficiente capacidad para recargar esa cantidad")

    def cuantas_tazas(self, capacidad_taza=200):
        # calcula la cantidad de tazas que se pueden servir con una cafetera. Recibe
        # el tamaño de la taza
        return self.__cant//capacidad_taza

    def vaciar_cafetera(self):
        self.__cant = 0

    def servir(self, cantidad):
        """Metodo para servir cafe
        Sirve cafe y lo descuenta de cantidad actual de cafe

        args
          cantidad (int): cantidad de café a servir.

        returns

        raises
                ValueError si no hay suficiente cafe
        """
        if self.__cant >= cantidad:
            self.__cant = self.__cant - cantidad
        else:
            raise ValueError("No hay suficiente cafe")

    def str_cant_sobre_capacidad(self):
        cadena = str(self.__cant) + "/" + str(self.__capacidad)
        return cadena

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def to_dict(self):
        """Devuelve los datos de la cafetera en forma de diccionario."""
        data = {
            "nombre_id": self.get_nombre(),
            "capacidad": self.get_capacidad(),
            "contenido": self.get_contenido(),
            "marca": self.get_marca(),
            "modelo": self.get_modelo(),
        }
        return data

    def get_datos(self):
        """Lo mismo que to_dict(), solo que respeta el nombre establecido en las especificaciones."""
        return self.to_dict()

    def set cafetera(self,nueva_capacidad, nueva_cant, nueva_marca, nuevo_modelo, nuevo_nombre_id):
        self.__capacidad = nueva_capacidad
        self.__cant = nueva_cant
        self.__marca = nueva_marca
        self.__modelo = nuevo_modelo
        self.__nombre_id = nuevo_nombre_id





class Cafeteria:
    def __init__(self, nombre):
        self.__lista_cafeteras = []
        self.__nombre = nombre

    def get_cantidad_cafeteras(self):
        return len(self.__lista_cafeteras)

    def buscar_cafetera_por_nombre(self, nombre):
        """
        Busca una cafetera dentro de la lista cafetera.
        args:
            nombre = nombre de la cafetera a bucar
        return:
            Un objeto cafetera
        """
        for item in self.__lista_cafeteras:
            if item.get_nombre() == nombre:
                return item
        return False

    def agregar_cafetera(self, cafetera: Cafetera):
        """
        Agrega una nueva cafetera a Cafeteria y la agrega
        a la lista lista_cafeteras
        arg:
            cafetera: Una clase cafetera para ser agregada
        return:
            True o False        
        """
        if isinstance(cafetera, Cafetera):
            # Si no encuentra la cafetera
            if not self.buscar_cafetera_por_nombre(cafetera.get_nombre()):
                self.__lista_cafeteras.append(cafetera)  # la agrega
                return True
            else:
                raise ValueError(
                    "La cafetera con ese nombre ya ha sido agregada")
                return False  # FIXME remover el return, no es necesario, dado que el error impide que se ejecute.
        else:  # No es un objeto cafetera
            raise ValueError("No es una cafetera válida. Agregue una cafetera")
            return False  #FIXME rEl return no es necesario, porque el error no permite que se alcance esa instrucción.


if __name__ == "__main__":
    pass
