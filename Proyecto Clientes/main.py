from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info, confirmar
)
from views import ClienteController, EstudianteController


class MenuClientes:
    """VISTA: muestra, pide y presenta. No decide reglas del negocio."""

    TITULO = "SISTEMA DE GESTIÓN DE CLIENTES"    
    ANCHO = 85

    def __init__(self, controlador=ClienteController):
        self._controlador = controlador
        self._activo = True
        self._opciones = {
            "1": ("Crear cliente", self.crear),
            "2": ("Ver todos", self.listar),
            "3": ("Buscar", self.buscar),
            "4": ("Ver por id", self.ver_por_id),
            "5": ("Actualizar", self.actualizar),
            "6": ("Eliminar", self.eliminar),
            "7": ("Estadísticas", self.estadisticas),
            "0": ("Salir", self.salir),
        }

    @staticmethod
    def pausa():
        input("\nPresione Enter para continuar...")

    @staticmethod
    def pedir_entero(etiqueta):
        """Devuelve un entero o None si el usuario escribió cualquier otra cosa."""
        try:
            return int(input(etiqueta))
        except ValueError:
            return None

    @staticmethod
    def mostrar_resultado(exito, mensaje):
        if exito:
            imprimir_exito(mensaje)
        else:
            imprimir_error(mensaje)

    def mostrar_tabla(self, clientes):
        print(f"{'ID':<5}{'NOMBRE':<25}{'EMAIL':<28}{'CIUDAD':<15}{'TELÉFONO':<12}")
        print("-" * self.ANCHO)
        for cliente in clientes:
            print(f"{cliente.id:<5}{cliente.nombre_completo:<25}"
                  f"{cliente.email:<28}{cliente.ciudad:<15}{cliente.telefono:<12}")
        print("-" * self.ANCHO)
        imprimir_info(f"Total: {len(clientes)} cliente(s)")

    def crear(self):
        imprimir_titulo("CREAR NUEVO CLIENTE")
        datos = {}
        for campo in self._controlador.MODELO.CAMPOS:
            datos[campo] = input(f"{campo.capitalize()}: ")

        exito, mensaje = self._controlador.crear(datos)
        self.mostrar_resultado(exito, mensaje)
        self.pausa()

    def listar(self):
        imprimir_titulo("LISTA DE CLIENTES")
        clientes = self._controlador.listar()
        if not clientes:
            imprimir_info("Todavía no hay clientes. Use la opción 1 para crear el primero.")
        else:
            self.mostrar_tabla(clientes)
        self.pausa()

    def buscar(self):
        imprimir_titulo("BUSCAR CLIENTE")
        termino = input("Nombre, email, teléfono o ciudad: ")
        encontrados = self._controlador.buscar(termino)
        if not encontrados:
            imprimir_info(f"Ningún cliente coincide con '{termino}'.")
        else:
            self.mostrar_tabla(encontrados)
        self.pausa()

    def ver_por_id(self):
        imprimir_titulo("VER CLIENTE POR ID")
        id_cliente = self.pedir_entero("Id del cliente: ")
        if id_cliente is None:
            imprimir_error("El id debe ser un número entero")
            return self.pausa()

        cliente = self._controlador.obtener(id_cliente)
        if cliente is None:
            imprimir_error(f"No existe un cliente con id {id_cliente}")
        else:
            self.mostrar_detalle(cliente)
        self.pausa()

    def mostrar_detalle(self, cliente):
        for clave, valor in cliente.a_diccionario().items():
            print(f"  {clave.capitalize():<12}: {valor}")
        imprimir_info(f"Dominio del email: {cliente.dominio_email}")

    def actualizar(self):
        imprimir_titulo("ACTUALIZAR CLIENTE")
        id_cliente = self.pedir_entero("Id del cliente: ")
        if id_cliente is None:
            imprimir_error("El id debe ser un número entero")
            return self.pausa()

        cliente = self._controlador.obtener(id_cliente)
        if cliente is None:
            imprimir_error(f"No existe un cliente con id {id_cliente}")
            return self.pausa()

        imprimir_info(f"Editando a {cliente.nombre_completo}")
        print("Deje en blanco el campo que no quiera cambiar.\n")

        cambios = {}
        for campo in self._controlador.MODELO.CAMPOS:
            actual = getattr(cliente, campo)          
            nuevo = input(f"{campo.capitalize()} [{actual}]: ").strip()
            if nuevo:
                cambios[campo] = nuevo

        self.mostrar_resultado(*self._controlador.actualizar(id_cliente, cambios))
        self.pausa()

    def eliminar(self):
        imprimir_titulo("ELIMINAR CLIENTE")
        id_cliente = self.pedir_entero("Id del cliente: ")
        if id_cliente is None:
            imprimir_error("El id debe ser un número entero")
            return self.pausa()

        cliente = self._controlador.obtener(id_cliente)
        if cliente is None:
            imprimir_error(f"No existe un cliente con id {id_cliente}")
            return self.pausa()

        imprimir_info(f"Se eliminará: {cliente}")
        if confirmar("¿Confirma la eliminación?"):
            self.mostrar_resultado(*self._controlador.eliminar(id_cliente))
        else:
            imprimir_info("Operación cancelada")
        self.pausa()

    def estadisticas(self):
        imprimir_titulo("ESTADÍSTICAS")
        datos = self._controlador.estadisticas()
        print(f"  Clientes registrados : {datos['total']}")
        print(f"  Ciudades distintas   : {len(datos['ciudades'])} -> {', '.join(datos['ciudades'])}")
        print(f"  Dominios de email    : {', '.join(datos['dominios'])}")
        print(f"  Sin teléfono         : {len(datos['sin_telefono'])}")
        self.pausa()

    def salir(self):
        self._activo = False          
        imprimir_info("¡Hasta luego! 👋")

    def mostrar_menu(self):
        imprimir_titulo(self.TITULO)
        for tecla, (texto, _metodo) in self._opciones.items():
            print(f"  {tecla}. {texto}")
        print()

    def ejecutar(self):
        """El bucle principal: vive mientras __activo sea True."""
        while self._activo:
            self.mostrar_menu()
            tecla = input("Seleccione una opción: ").strip()

            if tecla not in self._opciones:
                imprimir_error("Opción no válida")
                self.pausa()
                continue

            _texto, metodo = self._opciones[tecla]
            metodo()          


class MenuEstudiantes(MenuClientes):
    """Hereda todo el menú. Solo cambia lo que es distinto en estudiantes."""

    TITULO = "SISTEMA DE GESTIÓN DE ESTUDIANTES"     

    def __init__(self, controlador=EstudianteController):
        super().__init__(controlador)          
        self._opciones["1"] = ("Crear estudiante", self.crear)
        salir = self._opciones.pop("0")
        self._opciones["8"] = ("Agregar nota", self.agregar_nota)
        self._opciones["9"] = ("Ver promedio", self.ver_promedio)
        self._opciones["10"] = ("Materias en común", self.materias_en_comun)
        self._opciones["0"] = salir

    def agregar_nota(self):
        imprimir_titulo("AGREGAR NOTA")
        id_estudiante = self.pedir_entero("Id del estudiante: ")
        if id_estudiante is None:
            imprimir_error("El id debe ser un número entero")
            return self.pausa()

        materia = input("Materia: ")
        try:
            nota = float(input("Nota: "))
        except ValueError:
            imprimir_error("La nota debe ser un número")
            return self.pausa()

        self.mostrar_resultado(*self._controlador.agregar_nota(id_estudiante, materia, nota))
        self.pausa()

    def ver_promedio(self):
        imprimir_titulo("VER PROMEDIO")
        id_estudiante = self.pedir_entero("Id del estudiante: ")
        if id_estudiante is None:
            imprimir_error("El id debe ser un número entero")
            return self.pausa()

        estudiante = self._controlador.obtener(id_estudiante)
        if estudiante is None:
            imprimir_error(f"No existe un estudiante con id {id_estudiante}")
            return self.pausa()

        for materia in sorted(estudiante.materias):
            print(f"  {materia:<20}: {estudiante.notas_de(materia)}")
        imprimir_info(f"Promedio de {estudiante.nombre_completo}: {estudiante.promedio} ({estudiante.estado})")
        self.pausa()

    def materias_en_comun(self):
        imprimir_titulo("MATERIAS EN COMÚN")
        id_a = self.pedir_entero("Id del primer estudiante: ")
        id_b = self.pedir_entero("Id del segundo estudiante: ")

        exito, resultado = self._controlador.materias_en_comun(id_a, id_b)
        if not exito:
            imprimir_error(resultado)
        elif not resultado:
            imprimir_info("No tienen materias en común")
        else:
            imprimir_exito(f"En común: {', '.join(sorted(resultado))}")
        self.pausa()

    def mostrar_tabla(self, estudiantes):
        print(f"{'ID':<5}{'NOMBRE':<25}{'EMAIL':<28}{'CARNET':<15}{'PROMEDIO':<12}")
        print("-" * self.ANCHO)
        for estudiante in estudiantes:
            print(f"{estudiante.id:<5}{estudiante.nombre_completo:<25}"
                  f"{estudiante.email:<28}{estudiante.carnet:<15}{estudiante.promedio:<12}")
        print("-" * self.ANCHO)
        imprimir_info(f"Total: {len(estudiantes)} estudiante(s)")

    def mostrar_detalle(self, estudiante):
        for clave, valor in estudiante.a_diccionario().items():
            print(f"  {clave.capitalize():<12}: {valor}")
        imprimir_info(f"Promedio: {estudiante.promedio}")

if __name__ == "__main__":
    try:
        menus = {"1": MenuClientes, "2": MenuEstudiantes}
        eleccion = input("1. Clientes\n2. Estudiantes\nSeleccione un sistema: ").strip()
        menus.get(eleccion, MenuClientes)().ejecutar()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")