from formageometrica import FormaGeometrica
class Retangulo(FormaGeometrica):

    def __init__(self, largura:int, altura:int):
        super().__init__("Retângulo")
        self.__largura = largura
        self.__altura = altura

    def calcular_area(self)->str:
        return self.__largura * self.__altura

    def calcular_perimetro(self):
        return 2 * (self.__largura + self.__altura)







