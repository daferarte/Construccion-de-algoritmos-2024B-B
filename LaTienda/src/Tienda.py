__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Tienda:
    
    """----------------------------------------------------------------
    # Constructor
    ----------------------------------------------------------------"""
    __method__ = "Constructor"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "metodo constructor de la clase"
    def __init__(self):
        
        """----------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------"""
        self.__producto1 = None
        self.__producto2 = None
        self.__producto3 = None
        self.__producto4 = None 
        self.__dineroCaja:float = 0.0
        
    """----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------"""
    __method__ = "DarProducto1"
    __parameter__ = "Ninguno"
    __returns__ = "Producto1"
    __Description__ = "metodo que retorna la informacion de producto 1"
    def DarProducto1(self):
        return self.__producto1
    
    __method__ = "DarProducto2"
    __parameter__ = "Ninguno"
    __returns__ = "Producto2"
    __Description__ = "metodo que retorna la informacion de producto 2"
    def DarProducto2(self):
        return self.__producto2
    
    __method__ = "DarProducto3"
    __parameter__ = "Ninguno"
    __returns__ = "Producto3"
    __Description__ = "metodo que retorna la informacion de producto 3"
    def DarProducto3(self):
        return self.__producto3
    
    __method__ = "DarProducto4"
    __parameter__ = "Ninguno"
    __returns__ = "Producto4"
    __Description__ = "metodo que retorna la informacion de producto 4"
    def DarProducto4(self):
        return self.__producto4
    
    __method__ = "DarDineroCaja"
    __parameter__ = "Ninguno"
    __returns__ = "Dinero en caja"
    __Description__ = "metodo que retorna el dinero en caja"
    def DarDineroCaja(self):
        return self.__dineroCaja