#polimorfismo permite que obj de diferentes classes
#sejam tratados como objetos de uma classe comum

#tipo 1 - sobrescrita de método
class Cliente:
    def __init__(self,nome,celular):
        self.nome = nome
        self.celular = celular

    def show_info(self):
        print(f"nome:{self.nome},cel:{self.celular}")

class PessoaFisica(Cliente):
    def __init__(self,nome,celular,cpf):
        self.cpf = cpf
        super().__init__(nome,celular)

    def show_info(self):
        print(f"nome:{self.nome}, celular:{self.celular}, cpf:{self.cpf}")

class PessoaJuridica(Cliente):
    def __init__(self,nome,celular,cnpj):
        self.cnpj = cnpj
        super().__init__(nome,celular)

    def show_info(self):
        print(f"nome:{self.nome}, celular:{self.celular}, cnpj:{self.cnpj}")

pFisica = PessoaFisica("joao","119898888","09500000")
pJuridica = PessoaJuridica("Maria","11955555","00099998/0001")

pFisica.show_info()
pJuridica.show_info()

cliente = Cliente ("Jose","11977777777")
cliente.show_info()


# tipo 2 - Polimorfismo de Método
def mostrar_info_cliente(cliente):
    cliente.show_info()
print("==========================")
mostrar_info_cliente(pFisica)
mostrar_info_cliente(pJuridica)


# tipo 3 Polimorfismo de Função a mesma função operando com diferentes tipos de dados
def somar(a, b):
    return a + b

print(somar(5,5))
print(somar("Py","thon"))
print(somar(8.55,5.40))
print(somar([1,2,3],[4,5]))