import re
from datetime import datetime

class CadastroUsuario:
    def __init__(self, nome: str, cpf: str, nascimento: str, endereco: str, telefone: str, senha: str):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha

    def validar_nome(self):
        if not self.nome or len(self.nome.split()) < 2:
            raise ValueError("Nome inválido. Deve conter pelo menos nome e sobrenome.")
    
    def validar_cpf(self):
        padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        if not re.match(padrao_cpf, self.cpf):
            raise ValueError("CPF inválido. O formato correto é XXX.XXX.XXX-XX.")
    
    def validar_nascimento(self):
        try:
            data = datetime.strptime(self.nascimento, "%d/%m/%Y")
            if data > datetime.now():
                raise ValueError("Data de nascimento inválida. A data não pode ser no futuro.")
        except ValueError:
            raise ValueError("Data de nascimento inválida. O formato correto é DD/MM/AAAA.")
    
    def validar_endereco(self):
        if not self.endereco:
            raise ValueError("Endereço inválido. Não pode ser vazio.")
    
    def validar_telefone(self):
        padrao_telefone = r"^\(\d{2}\) \d{4,5}-\d{4}$"
        if not re.match(padrao_telefone, self.telefone):
            raise ValueError("Telefone inválido. O formato correto é (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.")
    
    def validar_senha(self):
        if len(self.senha) < 8 or not any(char.isdigit() for char in self.senha) or not any(char.isalpha() for char in self.senha):
            raise ValueError("Senha inválida. Deve conter pelo menos 8 caracteres, incluindo letras e números.")
    
    def validar_gravacao(self):
        self.validar_nome()
        self.validar_cpf()
        self.validar_nascimento()
        self.validar_endereco()
        self.validar_telefone()
        self.validar_senha()

    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Nascimento: {self.nascimento}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
    
    def gravar_info(self):
        self.validar_gravacao()
        nome_arquivo = f"cadastro_{self.cpf.replace('.', '').replace('-', '')}.txt"
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(f"Nome: {self.nome}\n")
            arquivo.write(f"CPF: {self.cpf}\n")
            arquivo.write(f"Nascimento: {self.nascimento}\n")
            arquivo.write(f"Endereço: {self.endereco}\n")
            arquivo.write(f"Telefone: {self.telefone}\n")
        print(f"Informações gravadas no arquivo {nome_arquivo}")
