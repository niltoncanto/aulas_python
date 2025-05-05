
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pacote1.classe1 import ClassOne
class ClassTwo:
    def __init__(self,teste):
        self.teste2 = teste

    def print_classe_one(self):
        print(f"ClassTwo: {self.teste2}")

class1 = ClassOne("teste1")