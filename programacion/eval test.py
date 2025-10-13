edad = int(input("Introduce la edad del jugador: "))

if edad < 10:
    print("Eres un niño")
elif edad >= 10 and edad < 20:
    print("Eres un adolescente")
elif edad >= 20 and edad < 30:
    print("Eres un joven")
else:
    print("Eres un adulto")