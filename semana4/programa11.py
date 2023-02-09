"""
    Programa11
    Nombre: Naomi Morales Sanchez
    Fecha: 09/02/2023
    Descrpción: Llamada o invocación
"""

def mayor(numero1:int,numero2:int)->int and None:
    result = None
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1:
        result = numero2
    return result

print(mayor(2, 1)) # 2
print(mayor(1, 2)) # 2
print(mayor(2, 2)) # None
print(mayor(2, -1)) # 2
print(mayor(-1, 2)) # 2
print(mayor(-1, -1)) # None
print(mayor(-2, -1)) # -1
print(mayor(-1, -2)) # -1
