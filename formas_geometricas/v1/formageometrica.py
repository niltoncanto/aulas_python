from abc import ABC, abstractmethod
from enum import Enum
import os

# Classe abstrata FormaGeometrica
class FormaGeometrica(ABC):

    def __init__(self, nome):
        self._nome = nome

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def __str__(self):
        return f"Forma: {self._nome}"

