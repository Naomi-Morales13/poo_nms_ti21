"""
    Nombre: Naomi Morales Sanchez
    Fecha: 13/02/2023
    Descripción: Clases con instancias
"""

class Persona:  #clase y solo imprime dos


    __nombre = None # Variable privada 

    def __init__(self): # Ejecutar la clase
        print("Persona") # Imprimira Persona

    def setNombre(self,nombre):  #modificar el valor
        self.__nombre = nombre # Guardamos el valor en la variable privada

    def getNombre(self): # Llama al valor
        return self.__nombre #regresa el valor        




dejah = Persona()
dejah.setNombre("Dejah")
print(dejah.getNombre())
