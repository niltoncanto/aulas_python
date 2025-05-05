
from circulo import Circulo
from retangulo import Retangulo
from gerenciararquivo import GerenciarArquivo

# Script Principal
if __name__ == "__main__":
    circulo = Circulo(5)
    retangulo = Retangulo(4, 6)

    print(circulo)
    print(retangulo)

    GerenciarArquivo.gravar(str(circulo))
    GerenciarArquivo.gravar(str(retangulo))

    print("\nDados lidos do arquivo:")
    print(GerenciarArquivo.ler())