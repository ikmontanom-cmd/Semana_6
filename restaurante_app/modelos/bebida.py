from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, disponibilidad, tamaño):
        super().__init__(nombre, precio, disponibilidad)
        self.tamaño = tamaño

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "No disponible"

        return (
            f"Bebida: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Disponibilidad: {estado}\n"
            f"Tamaño: {self.tamaño} ml"
        )