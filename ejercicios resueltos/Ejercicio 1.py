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