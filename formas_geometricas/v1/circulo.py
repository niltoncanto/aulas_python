from formageometrica import FormaGeometrica
import numpy as np
# Subclasse Circulo
class Circulo(FormaGeometrica):

    def __init__(self, raio):
        super().__init__("Círculo")
        self.__raio = raio

    def calcular_area(self):
        return np.pi * self.__raio * self.__raio

    def calcular_perimetro(self):
        return 2 * np.pi * self.__raio

    def __str__(self):
        return super().__str__() + f", Raio: {self.__raio}, Área: {self.calcular_area()}, Perímetro: {self.calcular_perimetro()}"

