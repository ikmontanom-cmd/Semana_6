from modelos.producto import Producto

class Platillo(Producto): 
    def __init__(self, nombre, precio, disponibilidad, calorias):
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias
        
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "No disponible"
        
        return (
            f"Platillo: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Disponibilidad: {estado}\n"
            f"Calorías: {self.calorias} kcal"
        )
       
            

    