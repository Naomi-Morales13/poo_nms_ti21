"""
    Programa11
    Nombre: Naomi Morales Sanchez
    Fecha: 09/02/2023
    Descrpción: Llamada o invocación
"""

def mayor(numero1:int,numero2:int)->int and None: # Se Definine una función con dos parametros, especificando el tipo de dato junto con el de salida
    result = None # se utiliza para indicar que una variable o expresión no tiene valor asignado.
    if numero1 > numero2: # Es para ver si numero1 es mayor
        result = numero1 # asigna el valor de la variable numero1 a la variable result.
    elif numero2 > numero1: # Es para ver si numero2 es mayor
        result = numero2 # asigna el valor de la variable numero2 a la variable result.
    return result # retornar el resultado

print(mayor(2, 1)) # 2
print(mayor(1, 2)) # 2
print(mayor(2, 2)) # None
print(mayor(2, -1)) # 2
print(mayor(-1, 2)) # 2
print(mayor(-1, -1)) # None
print(mayor(-2, -1)) # -1
print(mayor(-1, -2)) # -1
