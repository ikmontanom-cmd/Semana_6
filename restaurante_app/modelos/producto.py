class Producto: 
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.__precio = precio
        self.disponibilidad = disponibilidad
        
    def obtener_precio(self):
        return self.__precio
    
    def cambiar_precio(self, cambiar_precio):
        if cambiar_precio >= 0:
            self.__precio = cambiar_precio
        else:
            raise ValueError("El precio no puede ser negativo.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "No disponible"
        
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Disponibilidad: {estado}"
        )