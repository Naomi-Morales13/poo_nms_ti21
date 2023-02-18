"""
    Nombre: Naomi Morales Sanchez
    Fecha: 16/02/2023
    Descripción: Trabajar con clases en diferentes archivos

"""

class Persona: # Clase Persona

    __nombre = None

    def __init__(self) -> None: # Constructor de la clase persona
        print("Constructor Persona") # Imprime el texto "Constructor Persona"

    def setNombre(self, nombre:str)->None # Metodo para modificar el valor de la variable  
        self.__nombre = nombre # Asigna el valor de nombre a la variable privada __nombre

    def getNombre(self)->str: # Metodo para regresar el valor de la variable privada __nombre
        return self.__nombre # Regresa el valor de la variable privada __nombre

