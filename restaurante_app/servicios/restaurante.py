class Restaurante:
    """
    Gestiona los productos del restaurante.
    """

    def __init__(self, nombre, direccion, telefono):
        """
        Inicializa los datos del restaurante y las listas de platillos y bebidas.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.platillos = []
        self.bebidas = []

    def registrar_platillo(self, platillo):
        """
        Registra un nuevo platillo.
        """
        self.platillos.append(platillo)
        print("\nPlatillo registrado correctamente.")

    def registrar_bebida(self, bebida):
        """
        Registra una nueva bebida.
        """
        self.bebidas.append(bebida)
        print("\nBebida registrada correctamente.")

    def mostrar_productos(self):
        """
        Muestra todos los productos registrados.
        """
        print("\n========= PRODUCTOS =========")

        if not self.platillos and not self.bebidas:
            print("No existen productos registrados.")
            return

        print("\nDemostración del polimorfismo:\n")

        for platillo in self.platillos:
            platillo.mostrar_informacion()

        for bebida in self.bebidas:
            bebida.mostrar_informacion()