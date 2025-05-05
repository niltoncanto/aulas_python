# Classe responsável por submeter inscrição 
# Sempre que submeter a inscrição, verifica, por exemplo, se ela existe.   
class SubmeterInscricao:
    def __init__(self):
        self.consulta_inscricao = ConsultarInscricao()
    def submeter(self):
        if self.consulta_inscricao.consulta():
                print("Submetendo inscrição...")

# Classe responsável pela consulta da Inscrição
class ConsultarInscricao:
    def __init__(self):
        print("Visualizando inscrição")
    def consulta(self):
        print("Consultando inscrição...")

# Classe responsável pela impressão do comprovante
class ImprimirComprovante:
    def imprimir_comprovante(self):
        print("Imprimindo comprovativo da inscrição...")

# Testes
# Fazer uma consulta independente e imprimir ou não o comprovante
consulta = ConsultarInscricao()  # Instancia a classe de consulta
comprovante = ImprimirComprovante()  # Instancia a classe de impressão
# Chama o método de impressão separadamente
comprovante.imprimir_comprovante()


