"""
    programa6.py
    Nombre: Naomi Morales
    Fecha: 30/01/2023}
    Descripcion: Calcular Perimetro y area de un triangulo
"""
print("calcular area y perimetro de un triangulo") # imprimira area y perimetro
print("ingrese lo que se pide") # imprimira lo que se pide o una indicación

lado1 = float(input("Medida de lado 1: ")) # Pide valor
lado2 = float(input("Medida de lado 2: ")) # Pide valor
lado3 = float(input("Medida de lado 3: ")) # Pide valor

perimetro = lado1 + lado2 + lado3 # Va a operar las tres variables que vse ingresen haciendo su suma 
s = perimetro / 2 #  Almacena en la variable perimetro el resultado anterior y lo dividira entre 2
area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5 # Se calcula area

arear = round(area, 2) # Se redondea la area 

print("el perimetro del tiangulo es = {}".format(perimetro)) # imprime el perimetro
print("el area del triangulo es = {}".format(arear)) # imprime la area
