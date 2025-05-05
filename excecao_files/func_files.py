
class GerenciarFunc:
    def __init__(self,nome_arquivo):
        self.nome_arquivo = nome_arquivo
    def criar_arquivo(self):
        try:
            with open(self.nome_arquivo,"w",encoding="utf-8") as f:
                print("Arquivo criado com sucesso!")
        except Exception as e:
                print("Não foi possível criar o arquivo!")
    def adicionar_funcionario(self,nome,cargo):
        try:
            with open(self.nome_arquivo,"a",encoding="utf-8") as f:
                func = f"Nome:{nome} | cargo:{cargo}\n"
                f.write(func)
                print("funcionario adicionado com sucesso!")
        except Exception as e:
                print("Não foi possível adicionar o funcionario!")
    def listar_funcionarios(self):
        try:
            with open(self.nome_arquivo,"r",encoding="utf-8") as f:
                print("Lista de Funcionários:")
                for linha in f.readlines():
                    print(linha.strip())
        except Exception as e:
                print("Não foi possível ler o arquivo de funcionarios!")

def main():
    obj_gerenciar_func = GerenciarFunc("funcionarios.txt")
    obj_gerenciar_func.criar_arquivo()
    obj_gerenciar_func.adicionar_funcionario("Carlos","gerente")
    obj_gerenciar_func.adicionar_funcionario("Sandra","presidente")
    obj_gerenciar_func.listar_funcionarios()

main()





