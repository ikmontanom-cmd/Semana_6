from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n========== MENÚ RESTAURANTE ==========")
    print("1. Registrar platillo")
    print("2. Registrar bebida")
    print("3. Mostrar todos los productos")
    print("4. Salir")


def pedir_datos_comunes():
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    disponibilidad = input("¿Disponible? (s/n): ").strip().lower() == "s"
    return nombre, precio, disponibilidad


def main():
    restaurante = Restaurante(
        "Restaurante Delicioso",
        "Calle Principal 123",
        "555-1234"
    )

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre, precio, disponibilidad = pedir_datos_comunes()
            calorias = int(input("Calorías: "))
            platillo = Platillo(nombre, precio, disponibilidad, calorias)
            restaurante.registrar_platillo(platillo)   # <-- cambio aquí

        elif opcion == "2":
            nombre, precio, disponibilidad = pedir_datos_comunes()
            tamaño = int(input("Tamaño (ml): "))
            bebida = Bebida(nombre, precio, disponibilidad, tamaño)
            restaurante.registrar_bebida(bebida)   # <-- cambio aquí

        elif opcion == "3":
            restaurante.mostrar_productos()

        elif opcion == "4":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()