class Cliente():
    def __init__(self):
        self.email = None 
        self.nombre = None 
        self.direccion = None 

cliente1 = Cliente()
cliente1.email = "jese@empresa.com"
cliente1.nombre = "jose"
cliente1.direccion = "calle"   
     
print(cliente1.email)
print(cliente1.nombre)
print(cliente1.direccion)