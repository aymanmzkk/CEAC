class Cliente():
    def __init__(self):
        self.email = None 
        self.nombre = None 
        self.direccion = None 

cliente1 = Cliente()
cliente1.email = input("introduce el email del cliente: ")
cliente1.nombre = input("introduce el nombre del cliente: ")
cliente1.direccion = input("introduce la direccion del cliente: ")  
     
print(cliente1)
print(cliente1.email)
print(cliente1.nombre)
print(cliente1.direccion)