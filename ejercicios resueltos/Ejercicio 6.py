# Ejercicio 6 · Método de clase (fábrica)
# Agrega Cliente.desde_texto("1, Ana, Pérez, ana@x.com") que devuelva un objeto Cliente. Debe funcionar también
# si mañana existe ClienteVIP(Cliente).

class Cliente:
    def __init__(self, id_cliente, nombre, apellido, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    @classmethod
    def desde_texto(cls, linea):
        partes = [parte.strip() for parte in linea.split(",")]
        if len(partes) < 4:
            raise ValueError("Se esperaban al menos 4 datos separados por comas")
        id_cliente, nombre, apellido, email = partes[:4]
        return cls(int(id_cliente), nombre, apellido, email)

class ClienteVIP(Cliente):
    pass

c = ClienteVIP.desde_texto("1, Ana, Pérez, ana@x.com")
print(type(c).__name__)  
