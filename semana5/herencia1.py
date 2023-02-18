"""
Nombre: Naomi Morales Sanchez 
Fecha: 14/02/2023
Descripcion: Este programa es para analizar lo que es una herencia
"""

class Persona: # Se crea una clase

    __nombre = None # Variable Privada
    __edad = None # Variable Privada

    def __init__(self): # Metodo para almacenar todo lo de la clase
        print("Persona") # Imprimira Persona

    def setNombre(self,nombre): # Obtiene un valor 
        self.__nombre = nombre # Almacena el valor

class Alumno(Persona): # Se crea una nueva clase

    __matricula = None # Variable Privada
    __nombre = None # Variable Privada

    def __init__(self): # Metodo para almacenar todo lo de la clase
        super().__init__() # Llamamos a todo elemento de la super clase
        print("Alumno") # Imprimira Alumno



objeto_persona = Persona() # Instanciamos un objeto llamado objeto_persona
objeto_alumno = Alumno() # Instanciamos un objeto llamado objeto_alumno

print(dir(objeto_persona)) #Es pedir solo el directorio de metodos y variables
print(dir(objeto_alumno)) #Es pedir solo el directorio de metodos y variables

