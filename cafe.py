class Cafetera:
    
    def __init__(self, nombre_id,marca,modelo,tipo_de_cafe,capacidad=0, cant=0,funcionando="funcionando"):
        """crea el objeto de la clase cafetera"""
        self.__capacidad = capacidad
        self.__cant = cant
        self.__marca = marca
        self.__modelo = modelo
        self.__nombre_id = nombre_id
        self.__funcionando = funcionando
        self.__tipo_de_cafe = tipo_de_cafe
    
    def get_estado(self):
        """devuelve el estado"""
        if self.__funcionando=="funcionando":
            return True
        else:
            return False
    """devuelve el nombre de la cafetera"""        
    def get_nombre(self):
        """devuelve el nombre de la cafetera"""
        return self.__nombre_id

    def get_capacidad(self):
        """devuelve la capacidad de la cafetera""" 
        return self.__capacidad
       
    def get_contenido(self):
        """devuelve el contenido de la cafetera""" 
        return self.__cant
        
    def get_tipo_de_cafe():
        """devuelve el tipo de cafe que tiene la cafetera"""
        return self.__tipo_de_cafe      
        
    def get_admisible(self):
        """Retorna cuanto le falta a una cafetera para alcanzar su capacidad."""
        return self.get_capacidad() - self.get_contenido()

    def get_marca(self):
        """devuelve la marca"""
        return self.__marca

    def get_modelo(self):
        """devuelve el modelo"""
        return self.__modelo

    def set_contenido(self,cantidad):
            """cambia el contenido de capacidad"""
            self.__cant=cantidad

    def set_capacidad(self,capacidad):
            """cambia el contenido de capacidad"""
            self.__capacidad=capacidad        

    def esta_llena(self):
        # Si el elemento cafetera esta llena cap=cant devuelve true, sino devuelve false
        if self.get_capacidad() == self.get_contenido():
            return True
        else:
            return False
                
    def llenar_cafetera(self):
        """llena la cafetera"""
        self.set_contenido(self.get_capacidad())

    
    def recargar(self, cantidad):
        """metodo para recargar una cafetera, recibe la cantidad a recargar. Si se pasa dev. un error."""
        if self.get_estado():
            if cantidad <= get_admisible():
                self.set_contenido(self.get_contenido()+cantidad)
            else:
                raise ValueError(
                    "No hay suficiente capacidad para recargar esa cantidad")    
        else:
            raise Exception("Cafetera defectuosa, necesita mantenimiento")
            
         
    def cuantas_tazas(self, capacidad_taza=200):
        """calcula la cantidad de tazas que se pueden servir con una cafetera. Recibe
        el tamaño de la taza"""
        return self.get_contenido()//capacidad_taza

    """vacia la cafetera"""
    def vaciar_cafetera(self):
        self.set_contenido(0)
        
    def esta_vacia(self):
        """Retorna True si la cafetera no tiene cafe, caso contrario retorna False"""
        if self.get_capacidad() == self.get_admisible():
            return True
        else:
            return False    

    def servir(self, cantidad):
        """Metodo para servir cafe
        Sirve cafe y lo descuenta de cantidad actual de cafe

        args
          cantidad (int): cantidad de café a servir.

        returns

        raises
                ValueError si no hay suficiente cafe
        """
        if self.get_contenido() >= cantidad and get_estado():
            self.set_contenido(self.get_contenido() - cantidad)
        else:
            raise ValueError("En este momento no se puede servir cafe")
            

    def str_cant_sobre_capacidad(self):
        cadena = str(self.get_contenido()) + "/" + str(self.get_capacidad())
        return cadena

    def to_dict(self):
        """Devuelve los datos de la cafetera en forma de diccionario."""
        data = {
            "nombre_id": self.get_nombre(),
            "capacidad": self.get_capacidad(),
            "contenido": self.get_contenido(),
            "marca": self.get_marca(),
            "modelo": self.get_modelo(),
            "tipoCafe":self.get_tipo_de_cafe()
        }
        return data

    def get_datos(self):
        """Lo mismo que to_dict(), solo que respeta el nombre establecido en las especificaciones."""
        return self.to_dict()


class Cafeteria:
    
    def __init__(self, nombre):
        """crea una objeto Cafeteria"""
        self.__lista_cafeteras = []
        self.__nombre = nombre

    def get_nombre(self):
        """devuelve nombre de la cafeteria"""
        return self.__nombre
               
    def get_lista_cafetera(self):
        """devuelve la lista de cafeteras"""
        return self.__lista_cafeteras 

    def get_cantidad_cafeteras(self):
        """ devuelve la cantidad de cafeteras""" 
        return len(self.get_lista_cafetera())

    def buscar_cafetera_por_nombre(self, nombre):
        """
        Busca una cafetera dentro de la lista cafetera.
        args:
            nombre = nombre de la cafetera a bucar
        return:
            Un objeto cafetera
        """
        for item in self.get_lista_cafetera():
            if item.get_nombre() == nombre:
                return item
        return False


    def agregar_cafetera(self, cafetera:Cafetera):

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
                self.get_lista_cafetera().append(cafetera)  # la agrega
                return True
            else:
                raise ValueError(
                    "La cafetera con ese nombre ya ha sido agregada")
                return False  # FIXME remover el return, no es necesario, dado que el error impide que se ejecute.
        else:  # No es un objeto cafetera
            raise ValueError("No es una cafetera válida. Agregue una cafetera")


    def quitar_cafetera_nombre(self, nombrecaf):
        """borra la cafetera por nombre"""
        cafet=self.buscar_cafetera_por_nombre(nombrecaf)
        if cafet:
            self.get_lista_cafetera().remove(cafetera_borrada)
            print("Se quito la cafetera : {}".format(cafet.get_nombre()))          
        else:
            print("No se encontró la cafetera {} en la lista.".format(nombrecaf))


if __name__ == "__main__":
    cafetera1 = Cafetera(nombre_id="xcv45",marca="olivetti",modelo=2016,tipo_de_cafe="Arabica",capacidad=2500, cant=1500,funcionando="funcionando")

    cafetera2 = Cafetera(nombre_id="xcv44",marca="Oster",modelo=2017,tipo_de_cafe="Robusto",capacidad=2500, cant=1800,funcionando="funcionando")

    cafetera3 = Cafetera(nombre_id="xcv46",marca="olivetti",modelo=2016,tipo_de_cafe="Arabica",capacidad=0, cant=0,funcionando="funcionando")

    cafeteria = Cafeteria("cafeteria00")

    print("a")
    cafeteria.agregar_cafetera(cafetera1)
    print(cafeteria.get_lista_cafetera()[0].get_nombre())
    cafeteria.agregar_cafetera(cafetera2)
    print(cafeteria.get_lista_cafetera()[1].get_nombre())
