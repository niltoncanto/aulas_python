import pyodbc

# Classe abstrata Servico
class Servico:
    def __init__(self, tipo_servico, descricao):
        self._tipo_servico = tipo_servico  # atributo protegido
        self._descricao = descricao  # atributo protegido
    
    # Método abstrato retorna_orcamento
    def retorna_orcamento(self, valor_hora, horas):
        pass

# Subclasse ServicoInterno
class ServicoInterno(Servico):
    def __init__(self, tipo_servico, descricao, setor, horas):
        super().__init__(tipo_servico, descricao)  # chamada ao construtor da superclasse
        self._setor = setor  # atributo protegido
        self._horas = horas  # atributo protegido
    
    # Implementação do método abstrato retorna_orcamento
    def retorna_orcamento(self, valor_hora):
        return valor_hora * self._horas * 0.5  # 50% do valor da tabela

# Subclasse ServicoExterno
class ServicoExterno(Servico):
    def __init__(self, tipo_servico, descricao, cliente, horas):
        super().__init__(tipo_servico, descricao)  # chamada ao construtor da superclasse
        self._cliente = cliente  # atributo protegido
        self._horas = horas  # atributo protegido
    
    # Implementação do método abstrato retorna_orcamento
    def retorna_orcamento(self, valor_hora):
        return valor_hora * self._horas  # 100% do valor da tabela

# Classe concreta GerenciadorServicos
class GerenciadorServicos:
    # Conexão com o banco de dados
    def __init__(self):
        server = 'tcp:aulas.database.windows.net'
        database = 'aulas'
        user = "aluno"
        password = "ShuPez@12tZHT"
        port = "1433"

        # String de conexão
        connection_string = f'DRIVER={{SQL Server}};SERVER={server},{port};DATABASE={database};UID={user};PWD={password}'
        self.conn = pyodbc.connect(connection_string)
        
    # Inserir serviço interno
    def inserir_servico_interno(self, servico):
        cursor = self.conn.cursor()
        query = "INSERT INTO ServicosInternos (tipo_servico, descricao, setor, horas) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (servico._tipo_servico, servico._descricao, servico._setor, servico._horas))
        self.conn.commit()
        
    # Inserir serviço externo
    def inserir_servico_externo(self, servico):
        cursor = self.conn.cursor()
        query = "INSERT INTO ServicosExternos (tipo_servico, descricao, cliente, horas) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (servico._tipo_servico, servico._descricao, servico._cliente, servico._horas))
        self.conn.commit()
        
    # Listar serviços internos
    def listar_servicos_internos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ServicosInternos")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
    # Listar serviços externos
    def listar_servicos_externos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ServicosExternos")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
    # Buscar custo por hora de um serviço
    def buscar_custo_hora_servico(self, tipo_servico):
        cursor = self.conn.cursor()
        query = "SELECT valor_hora FROM PrecoServicos WHERE tipo_servico = ?"
        cursor.execute(query, (tipo_servico,))
        row = cursor.fetchone()
        return row[0] if row else None

# Exemplo de uso
gerenciador = GerenciadorServicos()

# Inserir um serviço interno
si = ServicoInterno("Manutenção básica", "Conserto de ventilador", "Setor A", 2)
gerenciador.inserir_servico_interno(si)

# Inserir um serviço externo
se = ServicoExterno("Reparo avançado", "Conserto de impressora", "Cliente X", 3)
gerenciador.inserir_servico_externo(se)

# Listar serviços
print("Serviços Internos:")
gerenciador.listar_servicos_internos()
print("\nServiços Externos:")
gerenciador.listar_servicos_externos()