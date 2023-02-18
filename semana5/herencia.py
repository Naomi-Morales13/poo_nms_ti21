"""
    Nombre: Naomi Morales Sanchez 
    Fecha: 14/02/2023
    Descripción: Este programa es para analizar lo que es una herencia y con varias subclases
"""

class Persona: # Se crea una clase
    def __init__(self): # Se almacena todo lo de la clase
        print("Persona") # Imprime Persona

class Alumno(Persona): # Se creó otra clase
    def __init__(self): # Se almacena todo lo de la clase
        super().__init__() # Llamamos a todo elemento de la super clase
        print("Alumno") # Imprimira Alumno



objeto_persona = Persona() # Crea un objeto de la clase Persona e invoca al constructor
objeto_alumno = Alumno() # Crea un objeto de la clase Alumno e invoca al constructor
