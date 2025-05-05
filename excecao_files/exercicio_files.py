class GerenciarArquivos:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    # Método para criar ou sobrescrever o arquivo com registros iniciais
    def criar_arquivo(self):
        try:
            with open(self.nome_arquivo, 'w') as arquivo:  # Modo 'w' para sobrescrever o arquivo
                print("Arquivo criado com sucesso!\n")
        except Exception as e:
            print(f"Erro ao criar o arquivo: {e}")

    # Método para adicionar novos funcionários ao arquivo
    def adicionar_funcionario(self, nome, cargo):
        try:
            with open(self.nome_arquivo, 'a') as arquivo:  # Modo 'a' para adicionar ao final do arquivo
                arquivo.write(f"Nome: {nome}, Cargo: {cargo}\n")
            print(f"Funcionário {nome} adicionado com sucesso!\n")
        except Exception as e:
            print(f"Erro ao adicionar funcionário: {e}")

    # Método para exibir o conteúdo do arquivo
    def exibir_conteudo(self):
        try:
            with open(self.nome_arquivo, 'r') as arquivo:  # Modo 'r' para leitura do arquivo
                conteudo = arquivo.read()
                if conteudo:
                    print(f"Conteúdo do arquivo '{self.nome_arquivo}':\n")
                    print(conteudo)
                else:
                    print(f"O arquivo {self.nome_arquivo} está vazio.\n")
        except FileNotFoundError:
            print(f"Arquivo {self.nome_arquivo} não encontrado. Por favor, crie o arquivo primeiro.\n")
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

# Programa principal
def main():
    # Cria um objeto da classe GerenciarArquivos
    gerenciador = GerenciarArquivos('funcionarios.txt')

    # Criar ou sobrescrever o arquivo com registros iniciais
    gerenciador.criar_arquivo()
    
    # Adicionar novos funcionários
    while True:
        nome = input("Nome do funcionário: ")
        cargo = input("Cargo do funcionário: ")
        gerenciador.adicionar_funcionario(nome, cargo)
        continuar = input("Deseja adicionar outro funcionário? (s/n): ").lower()
        if continuar != 's':
            break
    
    # Exibir o conteúdo do arquivo
    gerenciador.exibir_conteudo()

# Execução do programa principal
if __name__ == "__main__":
    main()
