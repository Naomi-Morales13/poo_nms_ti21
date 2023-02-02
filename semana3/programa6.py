"""
    programa6.py
    Nombre: Naomi Morales
    Fecha: 30/01/2023}
    Descripcion: Calcular Perimetro y area de un triangulo
"""
print("calcular area y perimetro de un triangulo")
print("ingrese lo que se pide")

lado1 = float(input("Medida de lado 1: "))
lado2 = float(input("Medida de lado 2: "))
lado3 = float(input("Medida de lado 3: "))

perimetro = lado1 + lado2 + lado3
s = perimetro / 2
area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5

arear = round(area, 2)

print("el perimetro del tiangulo es = {}".format(perimetro))
print("el area del triangulo es = {}".format(arear))
