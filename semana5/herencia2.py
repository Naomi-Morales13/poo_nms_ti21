"""
Nombre: Naomi Morales Sanchez 
Fecha: 14/02/2023
Descripcion: Herencia con diferentes tipos de clase heredando de Persona
"""

class Persona: #Se crea una clase

    __nombre = None  #Variable privada
    __edad = None  #Variable privada

    def __init__(self):  # almacenar todo lo de la clase
        print("Persona") # Imprimira Persona

    def setNombre(self,nombre): #Se obtiene un valor
        self.__nombre = nombre # Se almacena el valor

    def getNombre(self): # Lllama al valor
        return self.__nombre # Regresa el valor de la variable

    def setEdad(self,edad): # Modifica el valor de la variable
        self.__edad = edad # Asigna el valor

    def getEdad(self): # Llama al valor
        return self.__edad # Regresar el valor ingresado



class Alumno(Persona):  #Herencia

    __matricula = None  #Variable privada
    __nombre = None   #Variable privada

    def __init__(self):  #llamada a la clase o variable eso es self
        super().__init__()  #super es llamada a la super clase o es la que accede a la clase de lo que se hereda
        print("Alumno")  #imprime lo que esta en comillas

    def setMatricula(self,matricula):  #Se obtiene un valor
        self.__matricula = matricula # Se guarda el valor

    def getMatricula(self):  # Es una llamada del valor
        return self.__matricula  #Regresa el valor

    def setNombre(self,nombre): # Obtener un valor
        self.__nombre = nombre # Se guarda el valor

    def getNombre(self): # Es una llamada del valor
        return self.__nombre # Regresa el valor



class Profesor(Persona):
    __no_nomina = None  #Variable privada

    def __init__(self): # llamada a la clase o variable eso es self
        super().__init__() # super es llamada a la super clase o es la que accede a la clase de lo que se hereda
        print("Profesor") #imprime lo que esta en comillas

    def setNoNomina(self,no_nomina): # Obtener un valor
        self.__no_nomina = no_nomina # Se guarda el valor

    def getNoNomina(self): # Es una llamada del valor
        return self.__no_nomina # Regresa el valor

    

class Coordinador(Persona):
    __no_nomina = None  #Variable privada
    __carrera_a_cargo = None  #Variable privada

    def __init__(self): # llamada a la clase o variable eso es self
        super().__init__() # super es llamada a la super clase o es la que accede a la clase de lo que se hereda
        print("Coordinador") #imprime lo que esta en comillas

    def setNoNomina(self,no_nomina): # Modifica el valor de la variable privada
        self.__no_nomina = no_nomina # Asigna un nuevo valor a la variable privada

    def getNoNomina(self):  # Metodo para regresar el valor de la variable privada
        return self.__no_nomina  # Devuelve el valor de la variable privada

    def setCarreraCargo(self,carrera_a_cargo): # Modifica el valor de la variable privada
        self.__carrera_a_cargo = carrera_a_cargo # Asigna un nuevo valor a la variable privada

    def getCarreraCargo(self): # Metodo para regresar el valor de la variable privada
        return self.__carrera_a_cargo  # Devuelve el valor de la variable privada



objeto_persona = Persona() # Instanciamos un objeto llamado objeto_persona
objeto_alumno = Alumno() # Instanciamos un objeto llamado objeto_alumno
objeto_profesor = Profesor() # Instanciamos un objeto llamado objeto_profesor
objeto_coordinador = Coordinador() # Instanciamos un objeto llamado objeto_coordinador

  #print(dir(objeto_persona)) 
  #print(dir(objeto_alumno))
  #print(dir(objeto_profesor))
  #print(dir(objeto_coordinador))
