# Ejercicio 5 · Método estático
# Agrega a Cliente el método estático es_telefono_valido(texto): válido si está vacío o si son exactamente 10 dígitos. 
# Úsalo en el setter de telefono.
class Cliente:
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