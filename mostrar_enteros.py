import math 

def calcular_cuadrados(n):
    
    for i in range(1, n + 1):
        cuadrado = 0
        for j in range(1, (2 * i), 2):
            cuadrado += j
        print(f"Entero: {i}, Cuadrado: {cuadrado}")

# Solicitar el valor de n al usuario
n = int(input("Ingrese un número entero positivo: "))
calcular_cuadrados(n)
