while True:
    print("dime lo quieres hacer: ")
    print("1.-introduce un nuevo contacto")
    print("2.-leer todos los contactos")
    opcion = int(input("escoge tu opcion: "))
    if opcion == 1:
        nombre = input("introduce el nombre de la persona: ")
        email = input("introduce el email de la persona: ")
        archivo = open("agenda.txt",'a')
        archivo.write(nombre+","+email+"\n")
        archivo.close()
    elif opcion == 2:
        archivo = open("agenda.txt",'r')
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
        archivo.close()