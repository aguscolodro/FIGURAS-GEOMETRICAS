from PUNTOS import PUNTO
from Diagonales import Diagonales
class Ingresar:
    lista = []

    def ingresarCantidadPuntos(self):
        self.cantidad = eval(input("Ingrese la cantidad de puntos: "))
        for i in range(0, self.cantidad):
            punto = self.ingresarPuntos()
            self.lista = self.lista + [punto]
        return self.lista

    def getCantidad(self):
        return self.cantidad

    def ingresarPuntos(self):
        print("Ingrese los valores del punto:")
        x = eval(input("Valor de x: "))
        y = eval(input("Valor de y: "))
        return PUNTO(x,y)



ingresar = Ingresar()
lista = ingresar.ingresarCantidadPuntos()
diagonales=Diagonales()
print(diagonales.determinarFigura(ingresar.getCantidad()))
print (lista)


