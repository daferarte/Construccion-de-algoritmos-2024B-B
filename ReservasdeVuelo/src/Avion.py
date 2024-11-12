__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from Silla import Silla

class Avion:
    
    # constantes 
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42
    
    # Atributos
    def __init__(self):
        
        self.__sillasEjecutivas:Silla = []
        self.__sillasEconomicas:Silla = []
        
        # sillas ejecutivas 
        
        self.__sillasEjecutivas[0] = Silla(1, 1, 1)
        self.__sillasEjecutivas[1] = Silla(2, 1, 2)
        self.__sillasEjecutivas[2] = Silla(3, 1, 2)
        self.__sillasEjecutivas[3] = Silla(4, 1, 1)
        self.__sillasEjecutivas[4] = Silla(5, 1, 1)
        self.__sillasEjecutivas[5] = Silla(6, 1, 2)
        self.__sillasEjecutivas[6] = Silla(7, 1, 2)
        self.__sillasEjecutivas[7] = Silla(8, 1, 1)
        # sillas economicas
       CreacionSillasEconomicas()  # type: ignore
       
    __method__ = "CreacionSillasEconomicas"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = " metodo que crea las sillas economicas" 
    def CreacionSillasEconomicas(self):
        
        for i in range (self.SILLAS_ECONOMICAS):
            if (i+1)%3 == 0:
                self.__sillasEconomicas[i] = Silla((i+1), 2, 3)
            elif (i+1)%2 == 0:
                self.__sillasEconomicas[i] = Silla((i+1), 2, 2)
            else:
                self.__sillasEconomicas[i] = Silla((i+1), 2, 1)
                
    def EliminarReservas(self):
        
        for sillaEconomica in self.__sillasEconomicas:
            sillaEconomica.desasignarSilla()
            
        for sillaEjecutiva in self.__sillasEjecutivas:
            sillaEjecutiva.desasignarSilla()
            
            
            
        