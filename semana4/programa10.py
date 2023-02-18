"""
    Programa10
    Nombre: Naomi Morales Sanchez
    Fecha: 09/02/2023
    Descrpción: Llamada o invocación
"""


def mayor(numero1, numero2): # Se define una Funcion
    result = None # Variable None
    if numero1 > numero2: # Es una comparacion para ver si numero1 es mayor
        result = numero1 # obtiene el valor de numero1 en caso de ser verdadero
    elif numero2 > numero1: # Es una comparacion para ver si numero2 es mayor
        result = numero2 # obtiene el valor de numero1 en caso de ser verdadero
    return result # Return es retornar el resultado


print(mayor(2, 1)) # 2
print(mayor(1, 2)) # 2 
print(mayor(2, 2)) # None
print(mayor(2, -1)) # 2
print(mayor(-1, 2)) # 2
print(mayor(-1, -1)) # None
print(mayor(-2, -1)) # -1
print(mayor(-1, -2)) # -1
