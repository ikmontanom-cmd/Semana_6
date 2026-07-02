class Restaurante:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.productos = []
        self.direccion = direccion
        self.telefono = telefono
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def mostrar_productos(self):
        print(self.mostrar_informacion())
        print("\n=======Productos disponibles=======")
        
        
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def mostrar_informacion(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Dirección: {self.direccion}\n"
            f"Teléfono: {self.telefono}"
        )