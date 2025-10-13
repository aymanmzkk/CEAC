'''
programa de constantes
(c) 2025 Ayman Mouzakki
este programa gestiona los constantes
'''
base_imponible = float(input("Introduce el valor de la base imponible: "))
total_iva = base_imponible * 0.21
total_factura = base_imponible + total_iva

print("Base imponible: ", base_imponible)
print("IVA (21%): ", total_iva)      
print("Total factura: ", total_factura) 
