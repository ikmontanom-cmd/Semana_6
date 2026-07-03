class Restaurante:
    """
    Gestiona los productos del restaurante.
    """

    def __init__(self, nombre, direccion, telefono):
        """
        Inicializa los datos del restaurante y la lista de productos.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []

    def registrar_platillo(self, platillo):
        """
        Registra un nuevo platillo.

        Args:
            platillo (Platillo): Objeto de tipo Platillo.
        """
        self.productos.append(platillo)
        print("\nPlatillo registrado correctamente.")

    def registrar_bebida(self, bebida):
        """
        Registra una nueva bebida.

        Args:
            bebida (Bebida): Objeto de tipo Bebida.
        """
        self.productos.append(bebida)
        print("\nBebida registrada correctamente.")

    def mostrar_productos(self):
        """
        Muestra todos los productos registrados.
        """
        print("\n========= PRODUCTOS =========")

        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\nDemostración del polimorfismo:\n")

        for producto in self.productos:
            print(producto.mostrar_informacion())
            print("-" * 30)