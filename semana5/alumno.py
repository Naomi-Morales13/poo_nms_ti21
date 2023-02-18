"""
    Nombre: Naomi Morales Sanchez
    Fecha: 13/02/2023
    Descripción: Clases con instancias
"""

class Persona:  #clase y solo imprime dos


    __nombre = None # Variable Privada
    __matricula = None #Variable Privada
    __carrera = None # Variable Privada

    def __init__(self): #Constructor de la clase Persona
        print("Persona") # Imprime el texto "Persona"

    def setNombre(self,nombre):  # Modificar el valor de la variable privada __nombre
        self.__nombre = nombre # Asigna el valor de la variable nombre a la variable privada

    def getNombre(self):  # Regresa el valor de la variable privada __nombre
        return self.__nombre # Regresa el valor de la variable privada __nombre

        
    def setMatricula(self,matricula):  #modificar el valor de la variable __matricula
        self.__matricula = matricula # Asigna el valor de la variable privada __matricula

    def getMatricula(self):  # Metodo para regresar el valor de la variable privada
        return self.__matricula # Regresa el valor de la variable __matricula

    def setCarrera(self,carrera):  # Modificar el valor de la variable privada
        self.__carrera = carrera # Asigna el valor

    def getCarrera(self):  # Metodo para regresar el valor de la variable
        return self.__carrera # Regresa el valor de la variable



dejah = Persona() # Se hace una copia o herencia 
dejah.setNombre("Naomi") # Modificar valor de variables
print(dejah.getNombre()) # "Naomi"
dejah.setMatricula("1722110691") # Modificar valor de variables
print(dejah.getMatricula()) # "1722110691"
dejah.setCarrera("Desarrollo de Software") # Modificar valor de variables
print(dejah.getCarrera()) # "Desarrollo de Software"

