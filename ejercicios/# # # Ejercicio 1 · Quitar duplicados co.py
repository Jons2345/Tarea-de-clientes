# # # Ejercicio 1 · Quitar duplicados conservando el orden
# # De ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"], obtén una lista sin repetidos respetando el orden de aparición.

lugares = ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"]
lugar = set()
lu = []

for l in lugares:
    if l not in lugar:
        lugar.add(l)
        lu.append(l)
        
print(lu)

# Ejercicio 2 · Contar con un diccionario
# Arma {"Quito": 2, "Guayaquil": 2, "Cuenca": 1} y muestra la ciudad más repetida.

ciudades = ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"]
ciudad = {}
for c in ciudades:
    ciudad[c] = ciudad.get(c, 0) + 1
        
print (ciudad)
print(max(ciudad, key=ciudad.get))

# Ejercicio 3 · Conjuntos en acción
# Con {"Ana","Luis","Sol","Marco"} y {"Luis","Marco","Ruth"}: ¿quiénes están en las dos?, ¿quiénes solo en la primera?, 
# ¿cuántas personas distintas hay?



# Ejercicio 4 · Propiedad calculada
# Agrega a Cliente la propiedad iniciales que devuelva "A.P." para “Ana Pérez”. No debe guardar nada: se calcula al leerla.


# Ejercicio 5 · Método estático
# Agrega a Cliente el método estático es_telefono_valido(texto): válido si está vacío o si son exactamente 10 dígitos. 
# Úsalo en el setter de telefono.


# Ejercicio 6 · Método de clase (fábrica)
# Agrega Cliente.desde_texto("1, Ana, Pérez, ana@x.com") que devuelva un objeto Cliente. Debe funcionar también
# si mañana existe ClienteVIP(Cliente).


# Ejercicio 7 · Atributo de clase
# Haz que Cliente lleve la cuenta de cuántos clientes se crearon y agrega el método de clase resumen() que devuelva "Se han creado N clientes".
# ¿Por qué resumen() no puede ser un método de instancia?


# Ejercicio 8 · Sobre el proyecto
# Agrega al Controlador el método de clase agrupar_por_ciudad() que devuelva {"Guayaquil": ["Ana", "Luis"], "Quito": ["Sol"]}, y
# muéstralo como opción 8 del menú.




