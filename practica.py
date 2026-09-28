# Ejercicio 1 · Quitar duplicados conservando el orden
# De ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"], obtén
# una lista sin repetidos respetando el orden de aparición.

ciudades = ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"]

vista = set()
orden = []
for ciudad in ciudades:
    if ciudad not in vista:
        vista.add(ciudad)
        orden.append(ciudad)

print(orden)


# Ejercicio 2 · Contar con un diccionario
# Arma {"Quito": 2, "Guayaquil": 2, "Cuenca": 1} y muestra la ciudad más repetida.

localidades = {"Quito": 2, "Guayaquil": 2, "Cuenca": 1}
conteo = {}
for ciudad in ciudades:
    conteo[ciudad] = conteo.get(ciudad, 0) + 1

print(conteo)
print(max(conteo, key=conteo.get))
                
# Ejercicio 3 · Conjuntos en acción
# Con {"Ana","Luis","Sol","Marco"} y {"Luis","Marco","Ruth"}: ¿quiénes están en las dos?, 
# ¿quiénes solo en la primera?, ¿cuántas personas distintas hay?

nombre1 = {"Ana","Luis","Sol","Marco"} 
nombre2 = {"Luis","Marco","Ruth"}

print(len(nombre1 | nombre2))
print(nombre1 & nombre2)
print(nombre1 - nombre2)


# Ejercicio 4 · Propiedad calculada
# Agrega a Cliente la propiedad iniciales que devuelva "A.P." para “Ana Pérez”.
# No debe guardar nada: se calcula al leerla.

class cliente:
    def __init__(self, nombre):
        self.nombre = nombre

@property
def iniciales(self):
    return f"{self.__nombre[0]}.{self.__apellido[0]}.".upper()
    




# Ejercicio 5 · Método estático
# Agrega a Cliente el método estático es_telefono_valido(texto): válido si está vacío o 
# si son exactamente 10 dígitos. Úsalo en el setter de telefono.



















