from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

restaurante = Restaurante(
    "Restaurante Delicioso",
    "Calle Principal 123",
    "555-1234"
    )

platillo1 = Platillo("Tacos al Pastor", 10.99, True, 300)
platillo2 = Platillo("Enchiladas Verdes", 12.99, True, 350)
bebida1 = Bebida("Coca Cola", 2.99, True, 500)
bebida2 = Bebida("Agua Mineral", 1.99, True, 500)

restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)

restaurante.mostrar_productos()