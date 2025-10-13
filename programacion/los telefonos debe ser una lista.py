class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []

cliente1 = Cliente()      
cliente1.nombre = "Jose"

print("el nombre del cliennte es:",cliente1.nombre)

cliente1.telefonos.append("35637599")
cliente1.telefonos.append("35390598")

print(cliente1.telefonos)