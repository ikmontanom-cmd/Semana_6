# Restaurante App - Sistema de Gestión de Productos

## 👨‍💻 Estudiante
Nombre: Isabel Katherine Montaño    

---

## 📌 Descripción del sistema

Este proyecto es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO).  
El sistema simula la gestión de productos en un restaurante, permitiendo registrar platillos y bebidas, almacenarlos en un sistema central y mostrar su información.

---

## 🏗️ Estructura del proyecto

restaurante_app/
├── modelos/
│ ├── init.py
│ ├── producto.py
│ ├── platillo.py
│ └── bebida.py
├── servicios/
│ ├── init.py
│ └── restaurante.py
├── main.py
└── README.md


---

## 🧠 Principios de POO aplicados

### 🔹 Herencia
Se utiliza la clase base `Producto`, de la cual heredan:
- `Platillo`
- `Bebida`

Esto permite reutilizar atributos como nombre, precio y disponibilidad.

---

### 🔹 Encapsulación
El atributo `__precio` está encapsulado en la clase `Producto`, evitando acceso directo desde fuera de la clase.  
Su acceso se realiza mediante métodos:
- `obtener_precio()`
- `cambiar_precio()`

---

### 🔹 Polimorfismo
El método `mostrar_informacion()` es sobrescrito en las clases `Platillo` y `Bebida`, permitiendo mostrar información diferente según el tipo de objeto.

---

## 🍽️ Clases del sistema

### Producto (Clase base)
Representa un producto general del restaurante.

### Platillo (Clase hija)
Representa un plato de comida con atributo adicional:
- Calorías

### Bebida (Clase hija)
Representa una bebida con atributo adicional:
- Tamaño o volumen

### Restaurante (Clase de servicio)
Administra la lista de productos y muestra la información registrada.

---

## ▶️ Ejecución del programa

Ejecutar el archivo:


---

## 🎯 Conclusión

Este proyecto permite comprender y aplicar los principios fundamentales de la Programación Orientada a Objetos en Python, mejorando la organización, reutilización y mantenimiento del código.

## ✍️ Reflexión

La Programación Orientada a Objetos permite organizar mejor el código mediante clases y objetos, facilitando la reutilización y el mantenimiento del sistema.  
En este proyecto, la aplicación de herencia, encapsulación y polimorfismo ayudó a estructurar un sistema más ordenado y realista para la gestión de productos en un restaurante.