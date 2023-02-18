"""
    Nombre: Naomi Morales Sanchez
    Fecha: 13/02/2023
    Descripción: Clases con instancias
"""

class Persona:  #clase y solo imprime dos


    __nombre = None # Variable Privada
    __email = None # Variable Privada

    def __init__(self): # Metodo para ejecutar la clase
        print("Persona") # Imprimira Persona

    def setNombre(self,nombre):  #modificar el valor
        self.__nombre = nombre # Se guarada el valor de la variable

    def getNombre(self): # Lllama al valor
        return self.__nombre #regresa el valor

        
    def setEmail(self,email):  #modificar el valor
        self.__email = email # Asignamos un valor a la variable

    def getEmail(self): # Llama al valor 
        return self.__email #regresa el valor



dejah = Persona() # Se crea una copia
dejah.setNombre("Dejah") # Se asigna un valor entre comillas 
print(dejah.getNombre()) # se llama a ese valor
dejah.setEmail("dejah@gmail.com") # Se asigna un correo
print(dejah.getEmail()) # se imprime el correo asignado


jhon = Persona() # Instancia de una clase
print(jhon.getNombre())  # Se accede a un atributo 

carthoris = Persona() # Instancia de una clase
carthoris.setNombre("Carthoris") # Se da un valor
print(carthoris.getNombre()) # se imprime el valor que fue asignado


yara = Persona() # Instancia de una clase
yara.setNombre("Yara") # Se da un valor
print(yara.getNombre()) # se imprime el valor que fue asignado
yara.setEmail("yaya@gmail.com") # Se asigna un valor
print(yara.getEmail()) # se imprime el valor que fue asignado
