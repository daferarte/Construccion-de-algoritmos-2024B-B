__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Pasajero:
    
    # constructor
    def __init__(self, cedula, nombre):
        self.__cedula = cedula
        self.__nombre = nombre
    # metodos
    
    __method__ = "DarCedula"
    __parameter__ = "Ninguno"
    __returns__ = "Cedula"
    __Description__ = " metodo que retorna la cedula del pasajero"
    def DarCedula(self):
        return self.__cedula
    
    __method__ = "ModificarCedula"
    __parameter__ = "Cedula"
    __returns__ = "Ninguno"
    __Description__ = " metodo que modifica la cedula"
    def ModificarCedula(self, cedula):
        self.__cedula = cedula
    
    __method__ = "DarNombre"
    __parameter__ = "Ninguno"
    __returns__ = "Nombre"
    __Description__ = " metodo que retorna la Nombre del pasajero"
    def DarNombre(self):
        return self.__nombre
    
    __method__ = "ModificarNombre"
    __parameter__ = "Nombre"
    __returns__ = "Ninguno"
    __Description__ = " metodo que modifica la Nombre"
    def ModificarNombre(self, nombre):
        self.__nombre = nombre
    
    
        
    