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

        Args:
            platillo (Platillo): Objeto de tipo Platillo.
        """
        self.platillos.append(platillo)
        print("\nPlatillo registrado correctamente.")

    def registrar_bebida(self, bebida):
        """
        Registra una nueva bebida.

        Args:
            bebida (Bebida): Objeto de tipo Bebida.
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
            print(platillo.mostrar_informacion())
            print("-" * 30)

        for bebida in self.bebidas:
            print(bebida.mostrar_informacion())
            print("-" * 30)