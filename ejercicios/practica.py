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
class Cliente:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
@property
def iniciales(self):
    return f"{self.__nombre[0]}.{self.__apellido[0]}.".upper()
    
ana = Cliente("Ana", "Pérez")
print(ana.iniciales)

# Ejercicio 5 · Método estático
# Agrega a Cliente el método estático es_telefono_valido(texto): válido si está vacío o 
# si son exactamente 10 dígitos. Úsalo en el setter de telefono.

@staticmethod
def es_telefono_valido(self, texto):
    texto = str(texto).strip()
    return texto == "" or (len(texto) == 10 and texto.isdigit())

@property
def telefono(self):
    return self._telefono

@telefono.setter
def telefono(self, valor):
    if not Cliente.es_telefono_valido(valor):
        raise ValueError("El teléfono debe estar vacío o tener exactamente 10 dígitos")
    self._telefono = valor 

# Ejercicio 6 · Método de clase (fábrica)
# Agrega Cliente.desde_texto("1, Ana, Pérez, ana@x.com") 
# que devuelva un objeto Cliente. Debe funcionar también si mañana existe ClienteVIP(Cliente).



# Ejercicio 7 · Atributo de clase
# Haz que Cliente lleve la cuenta de cuántos clientes se crearon
# y agrega el método de clase resumen() que devuelva "Se han creado N clientes".
# ¿Por qué resumen() no puede ser un método de instancia?

# Ejercicio 8 · Sobre el proyecto
# Agrega al Controlador el método de clase agrupar_por_ciudad() que devuelva
# {"Guayaquil": ["Ana", "Luis"], "Quito": ["Sol"]}, y muéstralo como opción 8 del menú.

# Ver solución









