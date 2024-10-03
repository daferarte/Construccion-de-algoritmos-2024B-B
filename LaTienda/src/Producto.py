__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

import constantes

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
    def __init__(self, valorUnitario:float, subsidiado: bool, calidad):
        
        """----------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------"""
        
        self.valorUnitario = valorUnitario
        self.subsidiado = subsidiado
        self.calidad = calidad
        """----------------------------------------------------------------
        # self.subsidiado = True 
        # self.subsidiado = False
        ----------------------------------------------------------------"""
    
    """----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------"""
    
    def CalcularPrecioPapeleria(self):
        
        # self.precio = self.valorUnitario + (self.valorUnitario * self.IVA_PAPELERIA)
        self.precio = self.valorUnitario + (self.valorUnitario * constantes.IVA_PAPELERIA)
        
        