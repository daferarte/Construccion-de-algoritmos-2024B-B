__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

import constantes
from Tipos import Tipo

class Producto:
    
    """----------------------------------------------------------------
    # Constantes
    ----------------------------------------------------------------"""
    
    IVA_PAPELERIA = 0.10
    IVA_SUPERMERCADO = 0.04
    IVA_FARMACIA = 0.12
    
    """----------------------------------------------------------------
    # Constructor
    ----------------------------------------------------------------"""
    __method__ = "Constructor"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "metodo constructor de la clase"
    def __init__(self, nombre, tipo, valorUnitario:float, cantidad:int, cantidadMinima:int, subsidiado: bool, calidad):
        
        """----------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------"""
        self.__nombre=nombre
        self.__tipo=tipo
        self.__valorUnitario = valorUnitario
        self.__subsidiado = subsidiado
        self.__calidad = calidad
        self.__cantidadBodega = cantidad
        self.__cantidadMinima = cantidadMinima
        self.__cantidadUnidadesVendidas = 0
        """----------------------------------------------------------------
        # self.subsidiado = True 
        # self.subsidiado = False
        ----------------------------------------------------------------"""
        # tipo = Tipo.DOGUERIA
    
    """----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------"""
    
    __method__ = "CalcularPrecioPapeleria"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "metodo que calcula el precio de un producto tipo papeleria"
    def CalcularPrecioPapeleria(self):
        
        # self.precio = self.valorUnitario + (self.valorUnitario * self.IVA_PAPELERIA)
        self.precio = self.valorUnitario + (self.valorUnitario * constantes.IVA_PAPELERIA)
        
    __method__ = "DarNombre"
    __parameter__ = "Ninguno"
    __returns__ = "Nombre del producto"
    __Description__ = "metodo que retorna el nombre del producto"
    def DarNombre(self):
        return self.__nombre
    
    __method__ = "DarTIpo"
    __parameter__ = "Ninguno"
    __returns__ = "Tipo del producto"
    __Description__ = "Retorna el tipo del producto"
    def DarTIpo(self):
        return self.__tipo
    
    __method__ = "DarValorUnitario"
    __parameter__ = "Ninguno"
    __returns__ = "Valor Unitario"
    __Description__ = "Retorna el Valor Unitario"
    def DarValorUnitario(self):
        return self.__valorUnitario
    
    __method__ = "DarCantidadBodega"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad Bodega"
    __Description__ = "Retorna la cantidad en bodega"
    def DarCantidadBodega(self):
        return self.__cantidadBodega
    
    __method__ = "DarCantidadMinima"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad Minima"
    __Description__ = "Retorna la cantidad minima en bodega"
    def DarCantidadMinima(self):
        return self.__cantidadMinima
        
    __method__ = "DarCantidadUnidadesVendidas"
    __parameter__ = "Ninguno"
    __returns__ = "CantidadUnidadesVendidas"
    __Description__ = "Retorna la cantidad de unidades vendidas"
    def DarCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    