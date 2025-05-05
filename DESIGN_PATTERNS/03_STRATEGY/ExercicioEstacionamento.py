import math
import time

class Veiculo:
    pass

class Passeio(Veiculo):
    pass

class Carga(Veiculo):
    pass

class ContaEstacionamento:
    HORA = 3600 * 1000  # em milissegundos
    DIA = HORA * 24
    MES = DIA * 30

    def __init__(self, veiculo, inicio, fim=0):
        self.veiculo = veiculo
        self.inicio = inicio
        self.fim = fim

    def valor_conta(self):
        atual = self.fim if self.fim != 0 else int(time.time() * 1000)
        periodo = self.inicio - atual

        if isinstance(self.veiculo, Passeio):
            if periodo < 12 * self.HORA:
                return 2.0 * math.ceil(periodo / self.HORA)
            elif 12 * self.HORA < periodo < 15 * self.DIA:
                return 26.0 * math.ceil(periodo / self.DIA)
            else:
                return 300.0 * math.ceil(periodo / self.MES)
        elif isinstance(self.veiculo, Carga):
            # Adicionar regras para veículos de carga
            pass
        # Adicionar regras para outros tipos de veículo
        return 0  # padrão se nenhum caso for aplicado

# Exemplo de uso:
veiculo_passeio = Passeio()
conta = ContaEstacionamento(veiculo_passeio, 1650932400000)
print(conta.valor_conta())
