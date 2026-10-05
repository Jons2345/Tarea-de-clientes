# Ejercicio 3 · Conjuntos en acción
# Con {"Ana","Luis","Sol","Marco"} y {"Luis","Marco","Ruth"}: ¿quiénes están en las dos?, ¿quiénes solo en la primera?, 
# ¿cuántas personas distintas hay?

a = {"Ana","Luis","Sol","Marco"}
b = {"Luis","Marco","Ruth"}

ambas = a & b
diferencia = a - b
todos = len(a | b)

print(sorted(ambas), sorted(diferencia), todos)