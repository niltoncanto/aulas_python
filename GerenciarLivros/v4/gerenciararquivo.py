class GerenciarArquivo:

    # Construtor da classe que inicializa o nome do arquivo
    def __init__(self, arquivo):
        self.arquivo = arquivo

    # Método para gravar dados no arquivo
    def gravarArq(self, dados):
        with open(self.arquivo, 'a') as file:  # Abre o arquivo no modo de anexação
            file.write(dados + '\n')  # Escreve os dados seguidos de uma nova linha
    
    # Método para ler todo o conteúdo do arquivo
    def lerArq(self):
        with open(self.arquivo, 'r') as file:  # Abre o arquivo no modo de leitura
            return file.read()  # Retorna todo o conteúdo do arquivo
        
    # Método para ler uma única linha do arquivo
    def lerLinha(self):
        with open(self.arquivo, 'r') as file:  # Abre o arquivo no modo de leitura
            return file.readline()  # Retorna a primeira linha do arquivo
        
    # Método para ler todas as linhas do arquivo e retorná-las como uma lista
    def lerLinhas(self):
        with open(self.arquivo, 'r') as file:  # Abre o arquivo no modo de leitura
            return file.readlines()  # Retorna uma lista com todas as linhas do arquivo
        
    def lerWhile(self):
        linhas = []  # Lista para armazenar as linhas lidas do arquivo

        with open(self.arquivo, 'r') as file:  # Abre o arquivo no modo de leitura
            linha = file.readline()  # Lê a primeira linha do arquivo

            # Enquanto houver conteúdo na linha
            while linha:
                linhas.append(linha.strip())  # Adiciona a linha à lista (strip() remove a quebra de linha)
                linha = file.readline()  # Lê a próxima linha do arquivo

        return linhas  # Retorna a lista de linhas
