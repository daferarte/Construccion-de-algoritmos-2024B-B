__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from enum import Enum

class Silla:
    
    # enumeraciones 
    class Clase(Enum):
        EJECUTIVA = 1
        ECONOMICA = 2
    
    class Ubicacion(Enum):
        
        VENTANA = 1
        CENTRO = 2
        PASILLO = 3
    
    
    # atributos
    
    def __init__(self, numero, clase:Clase, ubicacion:Ubicacion):
        self.__numero = numero
        self.__clase = clase
        self.__ubicacion = ubicacion
        self.__pasajero = None
    
    __method__ = "DarNumero"
    __parameter__ = "Ninguno"
    __returns__ = "Numero"
    __Description__ = " metodo que retorna el numero de la silla"
    def DarNumero(self):
        
        return self.__numero
    
    __method__ = "DarClase"
    __parameter__ = "Ninguno"
    __returns__ = "Clase"
    __Description__ = " metodo que retorna la clase de la silla"
    def DarClase(self):
        
        return self.__clase
    
    __method__ = "DarUbicacion"
    __parameter__ = "Ninguno"
    __returns__ = "Ubicacion"
    __Description__ = " metodo que retorna la ubicacion de la silla"
    def DarUbicacion(self):
        
        return self.__ubicacion
    
    __method__ = "DarPasajero"
    __parameter__ = "Ninguno"
    __returns__ = "Pasajero"
    __Description__ = " metodo que retorna el pasajero de la silla"
    def DarPasajero(self):
        return self.__pasajero
    
    __method__ = "ModificarNumero"
    __parameter__ = "Numero"
    __returns__ = "Ninguno"
    __Description__ = " metodo que cambia el numero de la silla"
    def ModificarNumero(self, numero):
        
        self.__numero = numero
    
    __method__ = "ModificarClase"
    __parameter__ = "Clase"
    __returns__ = "Ninguno"
    __Description__ = " metodo que cambia la clase de la silla"
    def ModificarClase(self, clase: Clase):
        
        self.__clase = clase
    
    __method__ = "ModificarUbicacion"
    __parameter__ = "Ubicacion"
    __returns__ = "Ninguno"
    __Description__ = " metodo que modifica la ubicacion de la silla"
    def ModificarUbicacion(self, ubicacion: Ubicacion):
        
        self.__ubicacion = ubicacion
    
    __method__ = "ModificarPasajero"
    __parameter__ = "Pasajero"
    __returns__ = "Ninguno"
    __Description__ = " metodo que Modifica el pasajero de la silla"
    def ModificarPasajero(self, pasajero):
        self.__pasajero = pasajero
        
    __method__ = "asignarPasajero"
    __parameter__ = "Pasajero"
    __returns__ = "Ninguno"
    __Description__ = " metodo que Modifica el pasajero de la silla"    
    def asignarPasajero(self, pasajero):
        
        self.__pasajero = pasajero
    
    __method__ = "desasignarSilla"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = " metodo que desasigna la silla del pasajero"   
    def desasignarSilla(self):
        
        self.__pasajero = None
    
    __method__ = "sillaAsignada"
    __parameter__ = "Ninguno"
    __returns__ = "Boolean true = ocupada, false = libre"
    __Description__ = " metodo que consulta si una silla esta asignada"   
    def sillaAsignada(self):
        return self.__pasajero != None
    
    
    