# Ejercicio 7 · Atributo de clase
# Haz que Cliente lleve la cuenta de cuántos clientes se crearon y agrega el método de clase resumen() que devuelva "Se han creado N clientes".
# ¿Por qué resumen() no puede ser un método de instancia?

class Cliente:
    total_creados = 0
    
    def __init__(self, id_cliente, nombre, apellido, email,
                     telefono="", ciudad="", direccion=""):
            self.__id = id_cliente        
            self.nombre = nombre
            self.apellido = apellido
            self.email = email
            self.telefono = telefono
            self.ciudad = ciudad
            self.direccion = direccion
            Cliente.total_creados += 1
            
    @classmethod
    def resumen(cls):
        return f"Se han creado {cls.total_creados} clientes"
    
    
c1 = Cliente(1, "Ana", "Pérez", "ana@mail.com")
c2 = Cliente(2, "Luis", "Mora", "luis@mail.com", ciudad="Quito")
print(Cliente.resumen()) 
