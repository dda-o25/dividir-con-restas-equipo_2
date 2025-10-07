"""
Andrés Enrique Jaime de la Rosa 763799  

Emiliano Mayorga Álvarez expediente 764147  

Julieta Núñez Pacheco 764729  

Sol Valeria González Castro 764533  

El propósito de este código es calcular el cociente y residuo de una divison por medio de sumas y restas
07/10/2025
"""

# Declaraciones
cociente = 0
residuo = 0

# Entradas
dividendo = float(input("Introduzca el dividendo: "))
divisor = float(input("Introduzca el divisor: "))

# Proceso
while dividendo>=divisor:
    dividendo = dividendo-divisor
    residuo = dividendo
    cociente = cociente +1
# Salidas
print(f"El cociente es {cociente}\nEl residuo es {residuo}")