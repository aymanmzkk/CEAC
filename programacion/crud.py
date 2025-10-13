print("programa de gestion de clientes v0.1 Ayman")

print("selecciona una opcion: ")
print("1.insertar un cliente")
print("2.listar clientes")
print("3.actualizar clientes")
print("4.eliminar clientes")

clientes = []

while True:

    opcion = input("escoge una opcion: ")
    opcion = int(opcion)
    if opcion == 1:
        print("vamos a insertar un cliente")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("introduce el nombre del cliente: ")
        nuevocliente.email = input("introduce el email1 del cliente: ")
        nuevocliente.direccion = input("introduce la direccion del cliente: ")
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("vamos a ver los clientes")    
        print(clientes)
    elif opcion == 3:
        print("vamos a actualizar los clientes")  
    elif opcion == 4:
        print("vamos a eliminar un cliente")      
    else:
      break    