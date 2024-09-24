__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

#----------------------------------------------------------------
# Importaciones
#----------------------------------------------------------------

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Asociaciones
    #----------------------------------------------------------------
    
    __cuentaAhorros=CuentaAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
        # Aqui inicia mi codigo
        self.__cuentaCorriente.ConsignarSaldo(monto)
    
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total actual en todas las cuentas"
    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        # total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        # return total
        # Metodo 2
        return self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite pasar saldo de la cuenta de ahorrros a la cuenta corriente"
    def PasarAhorroACorriente(self):
        # Aqui inicia mi codigo
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)