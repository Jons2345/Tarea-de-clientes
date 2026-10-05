# Ejercicio 4 · Propiedad calculada
# Agrega a Cliente la propiedad iniciales que devuelva "A.P." para “Ana Pérez”. No debe guardar nada: se calcula al leerla.

class Cliente:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre        
        self.__apellido = apellido    

    @property
    def iniciales(self):
        return f"{self.__nombre[0]}.{self.__apellido[0]}.".upper()


ana = Cliente("Ana", "Pérez")
print(ana.iniciales)   
