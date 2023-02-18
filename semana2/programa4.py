"""
    programa4.py
    Nombre: Naomi Morales Sanchez
    Fecha: 26/01/ 2023
    Descripción: se esta revisando la maera correcta e incorrecta de imprimir variables tipo int
"""
numero1 = 10 #variable de tipo int
numero2 = 5 #variable de tipo int
print("{} + {} = {}".format(numero1, numero2, numero1 + numero2)) # 10 + 5 = 15

# print("{} + {} = ".format(numero1, numero2, numero1 + numero2)) # 10 + 5 = 15

print("{n1} + {n2} = {suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2)) # La cadena final que se imprime mostrará los valores de numero1 y numero2, junto con su suma.

print("{numero1} + {numero2} = {suma}".format(numero1=numero1, numero2=numero2,suma=numero1+numero2)) # mostrará los valores de numero1 y numero2, junto con su suma.

# print("{numero1} + {numero2} = ".format(numero1, numero2, numero1+ numero2)) # 

# print("{n4} + {n4} = {suma}".format(n1= numero1, n2=numero2,suma=numero1+numero2)) no se encuentra la variable