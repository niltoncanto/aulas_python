
class Calculadora:
    def soma(self,*args):
        return sum(args)

    def div(self,a, b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Erro divisão por zero")
            return None

    # Exemplo de função em Python que utiliza **kwargs para aceitar um número arbitrário de argumentos de palavra-chave
    def exibir_informacoes(self,**kwargs):
        for chave, valor in kwargs.items():
            print(f"{chave}: {valor}")

calc = Calculadora()
print(calc.soma(1, 2, 3, 4,-5,6.75))
#print(calc.div(15,'b'))

# Chamada da função com argumentos de palavra-chave
calc.exibir_informacoes(nome="Carlos", idade=30, profissao="Engenheiro")
calc.exibir_informacoes(nome="Antonio", idade=40, profissao="Físico", sexo="M")