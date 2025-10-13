#Estás desarrollando un programa para registrar los resultados de un partido de fútbol.
#El programa debe almacenar información sobre el equipo, 
#el número de goles marcados y el número de goles recibidos.

nombre_de_equipo = ""
goles_marcados = 0
goles_recibidos = 0

nombre_de_equipo = "FCB"
goles_marcados = 1
goles_recibidos =1

print("El nombre del equipo:", nombre_de_equipo)
print("Cuantos goles marco el equipo:", goles_marcados)
print("Cuantos goles recibo el equipo:", goles_recibidos)

if goles_marcados > goles_recibidos:
    print("El equipo he ganado el partido")
elif goles_recibidos > goles_marcados:
    print("El equipo he perdido el partido")
elif goles_marcados == goles_recibidos:
    print("Empate!")