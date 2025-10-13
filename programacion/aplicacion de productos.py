'''
aplicacion de gestion de peoductos
esta aplicacion gestiona productos
'''

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0

productos = []

print("gestor de productos v0.1 Ayman")

while True:
    print("selecciona una opcion:")
    print("1.-Crear un nuevo producto")
    print("2.-Listar productos")
    print("3.-Actualizar productos")
    print("4.-Eliminar productos")

opcion = int(input("Escoge tu opcion: "))

if opcion == 1:
    print("Creamos un nuevo producto")
    producto = Producto()
    producto.nombre = input("Introduce el nombro del producto")
    producto.precio = input("Introduce el precio del producto")
    productos.appen(producto1)

elif opcion == 2:
    print("Vamos a listar productos")

elif opcion == 3:
    print("vamos a actualizar productos")

elif opcion == 4:
    print("vamos a eliminar productos")