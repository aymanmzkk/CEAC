class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
    def setNombreCompleto(self,nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email

clientes = []

print("gestor de clientes v0.1 ayman")
while True:
    print("selecciona una opcion:")
    print("1.-Insertar un nuevo cliente")
    print("2.- Obtener listado de clientes")
    opcion = int(input("indica tu opcion (1,2): "))

    if opcion == 1:
        print("Voy a insertar un cliente")
        nuevocliente = Cliente()
        nombrecliente = input("Introduce el nombre del cliente:")
        nuevocliente.setNombreCompleto(nombrecliente)
        emailcliente = input("introduce el email del cliente")
        nuevocliente.setEmail(emailcliente)
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("saco el listado de clientes")
        for cliente in clientes:
            print("--------------------")
            print("Nombre: ",cliente.getNombreCompleto())
            print("email: ",cliente.getEmail())
            print("--------------------")