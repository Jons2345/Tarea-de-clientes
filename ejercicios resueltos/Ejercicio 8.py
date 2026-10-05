# Ejercicio 8 · Sobre el proyecto
# Agrega al Controlador el método de clase agrupar_por_ciudad() que devuelva
# {"Guayaquil": ["Ana", "Luis"], "Quito": ["Sol"]}, y muéstralo como opción 8 del menú.

@ classmethod
def agrupar_por_ciudad(cls):
    agrupados = {}
    for objeto in cls.listar:
        ciudad = objeto.ciudad or "Sin ciudad"
        agrupados.setdefault(ciudad, []).append(objeto.nombre_completo)
    return agrupados


def por_ciudad(self):
    imprimir_titulo("CLIENTES POR CIUDAD")
    for ciudad, nombres in self.__controlador.agrupar_por_ciudad().items():
        print(f"  {ciudad}: {', '.join(nombres)}")
    self.pausa()


