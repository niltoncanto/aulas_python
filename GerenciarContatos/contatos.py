import sqlite3
from abc import ABC, abstractmethod

# Classe abstrata para representar um contato
class Contato(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    @abstractmethod #
    def obter_informacoes(self):
        pass #  Não faz nada  

# Classe para representar um contato pessoal
class ContatoPessoal(Contato):
    def __init__(self, nome, email, cel):
        super().__init__(nome, email)
        self.cel = cel

    # Sobrescrever o método abstrato
    def obter_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}, matricula: {self.matricula}"

# Classe para representar um contato profissional
class ContatoProfissional(Contato):
    def __init__(self, nome, email, cel, empresa, cargo):
        super().__init__(nome, email)
        self.cel = cel
        self.empresa = empresa
        self.cargo = cargo

    # Sobrescrever o método abstrato
    def obter_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}, Celular: {self.cel}, Empresa: {self.empresa}, Cargo: {self.cargo}"

# Classe para interagir com o banco de dados
class GerenciarContatos:
    def __init__(self, bd): # Recebe a conexão como parâmetro
           self.conexao = sqlite3.connect(bd)
           self.cursor = self.conexao.cursor()

    # Inserir contatos no banco de dados
    def inserir_contato_pessoal(self, contato):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO contatos (nome, email, cel) VALUES (?, ?, ?)", (contato.nome, contato.email, contato.cel))
            self.conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir contato pessoal: {str(e)}")
        finally:
            if cursor:
                cursor.close()

    # Inserir contatos no banco de dados
    def inserir_contato_profissional(self, contato):
        try: # Tenta executar o código
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO contatos (nome, email, cel, empresa, cargo) VALUES (?, ?, ?, ?, ?)",
                           (contato.nome, contato.email, contato.cel, contato.empresa, contato.cargo))
            self.conexao.commit()
        except Exception as e: # Se der erro, executa o código abaixo
            print(f"Erro ao inserir contato profissional: {str(e)}")
        finally:
            if cursor:
                cursor.close()

    # Listar contatos pessoais
    def listar_contatos_pessoais(self):
        try: #
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM contatos")
            contatos = cursor.fetchall()
            return contatos
        except Exception as e: # Se der erro, executa o código abaixo
            print(f"Erro ao listar contatos pessoais: {str(e)}")
            return []
        finally:
            if cursor:
                cursor.close()

    # Listar contatos profissionais
    def listar_contatos_profissionais(self):
        try: #  Tenta executar o código
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM contatos")
            contatos = cursor.fetchall()
            return contatos
        except Exception as e: #    Se der erro, executa o código abaixo
            print(f"Erro ao listar contatos profissionais: {str(e)}")
            return []
        finally:
            if cursor:
                cursor.close()

class Criar_BD:
    conexao = sqlite3.connect("contatos.db")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contatos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, cel TEXT, empresa TEXT, cargo TEXT);")
    conexao.commit()
    conexao.close()
    

if __name__ == "__main__":
    
    criarBD = Criar_BD()
    bd = GerenciarContatos("contatos.db")
    # Criação dos contatos, 
    contato_pessoal = ContatoPessoal("João ", "joao@gmail.com", "34343334")
    contato_profissional = ContatoProfissional("Maria", "maria@gmail.com", "987-654-3210", "IBM", "Diretora")

    # Inserir contatos no banco de dados
    bd.inserir_contato_pessoal(contato_pessoal)
    bd.inserir_contato_profissional(contato_profissional)

    # Listar contatos pessoais e profissionais
    print("Contatos Pessoais:")
    contatos_pessoais = bd.listar_contatos_pessoais()
    for contato in contatos_pessoais:
        print(contato)

    # Listar contatos pessoais e profissionais
    print("\nContatos Profissionais:")
    contatos_profissionais = bd.listar_contatos_profissionais()
    for contato in contatos_profissionais:
        print(contato)
