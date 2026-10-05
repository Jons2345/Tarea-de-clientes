
# Ejercicio 2 · Contar con un diccionario
# Arma {"Quito": 2, "Guayaquil": 2, "Cuenca": 1} y muestra la ciudad más repetida.

ciudades = ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"]
ciudad = {}
for c in ciudades:
    ciudad[c] = ciudad.get(c, 0) + 1
        
print (ciudad)
print(max(ciudad, key=ciudad.get))
