class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        """Getter para o nome."""
        return self._nome

    @nome.setter
    def nome(self, valor):
        """Setter para o nome, com alguma validação."""
        if isinstance(valor, str) and len(valor) > 0:
            self._nome = valor
        else:
            raise ValueError("O nome deve ser uma string não vazia.")

    @nome.deleter
    def nome(self):
        """Deleter para o nome. Aqui você adiciona a lógica ao deletar o nome."""
        print(f"Deletando nome: {self._nome}")
        del self._nome



numero = 10
print(isinstance(numero, int))  # Verifica se numero é um inteiro. Retorna True.

ponto_flutuante = 10.5
print(isinstance(ponto_flutuante, float))  # Verifica se ponto_flutuante é um float. Retorna True.

lista = [1, 2, 3]
print(isinstance(lista, list))  # Verifica se lista é uma lista. Retorna True.

dicionario = {'chave': 'valor'}
print(isinstance(dicionario, dict))  # Verifica se dicionario é um dicionário. Retorna True.

# Verificação múltipla
print(isinstance(ponto_flutuante, (int, float)))  # Verifica se ponto_flutuante é int ou float. Retorna True.
