"""
    programa8.py
    Nombre: Naomi Morales
    Fecha: 02/02/2023
    Descripcion: Elaboración de Unit Test
"""

numero1 = int(input("numero1")) #es un numero entero
numero2 = int(input("numero2")) #es un numero entero

if numero1 > numero2: #se hara la comparación
    print(numero1) # Imprime numero1 si es verdadero 
    
elif numero2 > numero1: # Se hace otra comparación
    print(numero2) # Imprime numero2 si es verdadero

else: 
    print(None) # Imprime None si son iguales
    