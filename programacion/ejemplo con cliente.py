class Cliente():
    def __init__(self,nombre,appelidos,email,direccion):
        self.nombre = nombre
        self.appelidos = appelidos
        self.email = email
        self.direccion = direccion

clientes = []
while True:

    nombre = input("Introduce el nombre del cliente: ")
    appelidos = input("Introduce los appelidos del cliente: ")
    email = input("Introduce el email del cliente: ")
    direccion = input("Introduce la direccion del cliente: ")

clientes.append(Cliente(nombre,appelidos,email,direccion))