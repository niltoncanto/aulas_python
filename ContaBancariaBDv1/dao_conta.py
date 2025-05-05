#data access object
class ContaBancariaDAO:
    def __init__(self, conn):
        self.conn = conn

    def salvar_conta(self, conta):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO contas (numero_conta, nome_titular, _saldo, __limite)
        VALUES (?, ?, ?, ?)
        ''', (conta.numero_conta, conta.nome_titular, conta.get_saldo(), conta.get_limite()))
        self.conn.commit()

    def listar_contas(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM contas')
        contas = cursor.fetchall()
        return contas
