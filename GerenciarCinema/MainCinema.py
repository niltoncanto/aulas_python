class Filme:
    def __init__(self, nome, duracao, classificacao_etaria):
        self.nome = nome
        self.duracao = duracao
        self.classificacao_etaria = classificacao_etaria

class Sala:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.filme_em_exibicao = None

    def exibir_filme(self, filme):
        self.filme_em_exibicao = filme
        print(f"Agora exibindo: {filme.nome}")

    def get_capacidade(self):
        return self.capacidade

if __name__ == "__main__":
    titanic = Filme("Titanic", 195, 12)
    sala1 = Sala(100)

    sala1.exibir_filme(titanic)
