from src.Empleado import Empleado

empleado1 = Empleado("Juan", "Perez", 1000000, 1)
print(empleado1.DarSalario())
print(empleado1.DarNombre())
print(empleado1.CalcularSalarioAnual())
print("----------------------------------------------------------------")
empleado1.CambiarSalario(2300000)
print(empleado1.CalcularSalarioAnual())
print(empleado1.CalcularImpuestoSalarioAnual())
