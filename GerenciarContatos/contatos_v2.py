import pyodbc
from datetime import date

# versão 2 - com herança, sem abstração
class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
      
    def obter_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"  

# Classe para representar um contato pessoal
class ContatoPessoal(Contato):
    def __init__(self, nome, email, telefone, data_aniversario):
        super().__init__(nome, email, telefone)
        self.data_aniversario = data_aniversario


    def obter_informacoes(self):
        return super().obter_informacoes() + f"Aniversário: {self.data_aniversario}"

# Classe para representar um contato profissional
class ContatoProfissional(Contato):
    def __init__(self, nome, email, telefone, empresa, cargo):
        super().__init__(nome, email, telefone)
        self.empresa = empresa
        self.cargo = cargo

    
    def obter_informacoes(self):
        return super().obter_informacoes() + f"Empresa: {self.empresa}, Cargo: {self.cargo}"

# Classe para interagir com o banco de dados
class GerenciarContatos:
    def __init__(self, conexao): # Recebe a conexão como parâmetro
        self.conexao = conexao

    # Inserir contatos no banco de dados
    def inserir_contato_pessoal(self, contato):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO ContatosPessoais (nome, email, telefone, data_aniversario) VALUES (?, ?, ?, ?)",
                           contato.nome, contato.email, contato.telefone, contato.data_aniversario.strftime('%Y-%m-%d'))
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
            cursor.execute("INSERT INTO ContatosProfissionais (nome, email, telefone, empresa, cargo) VALUES (?, ?, ?, ?, ?)",
                           (contato.nome, contato.email, contato.telefone, contato.empresa, contato.cargo))
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
            cursor.execute("SELECT * FROM ContatosPessoais")
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
            cursor.execute("SELECT * FROM ContatosProfissionais")
            contatos = cursor.fetchall()
            return contatos
        except Exception as e: #    Se der erro, executa o código abaixo
            print(f"Erro ao listar contatos profissionais: {str(e)}")
            return []
        finally:
            if cursor:
                cursor.close()

if __name__ == "__main__":
    # Configuração da conexão
    server = 'tcp:aulas.database.windows.net'
    database = 'aulas'
    user = "aluno"
    password = "ShuPez@12tZHT"
    port = "1433"

    # String de conexão
    conn_string = f'DRIVER={{SQL Server}};SERVER={server};PORT={port};DATABASE={database};UID={user};PWD={password}'
    
    # Criar conexão
    try: # Tenta executar o código
        conexao = pyodbc.connect(conn_string)
        print("Conexão bem-sucedida!")
    except Exception as e: # Se der erro, executa o código abaixo
        print(f"Erro ao acessar o banco: {e}")

    # Criação dos contatos, 
    contato_pessoal = ContatoPessoal("João ", "joao@gmail.com", "123-456-7890", date(1990, 5, 15))
    contato_profissional = ContatoProfissional("Maria", "maria@gmail.com", "987-654-3210", "IBM", "Diretora")

    # Conexão com o banco de dados
    bd = GerenciarContatos(conexao)

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
