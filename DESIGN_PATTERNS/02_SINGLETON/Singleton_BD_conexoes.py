import threading
import queue
import time
import logging

# Configura o nível de logging para exibir mensagens de informações
logging.basicConfig(level=logging.INFO)

class DatabaseConnection:
    def __init__(self, id):
        """Representa uma conexão individual com o banco de dados."""
        self.id = id          # Identificador único da conexão
        self.in_use = False    # Flag para verificar se a conexão está em uso

class DatabaseConnectionPool:
    _instance = None           # Armazena a única instância da classe (Singleton)
    _lock = threading.Lock()    # Lock para controle de acesso entre threads

    def __new__(cls, max_connections=5):
        """Garante uma única instância do pool usando o padrão Singleton."""
        if cls._instance is None:  # Verifica se a instância já foi criada
            with cls._lock:        # Bloqueia para garantir que apenas uma thread acesse este bloco
                if cls._instance is None:  # Verifica novamente para evitar criação concorrente
                    cls._instance = super(DatabaseConnectionPool, cls).__new__(cls)
                    cls._instance._init_pool(max_connections)  # Inicializa o pool de conexões
        return cls._instance

    def _init_pool(self, max_connections):
        """Inicializa o pool de conexões e a fila de espera."""
        self.max_connections = max_connections                     # Define o número máximo de conexões
        self.connections = [DatabaseConnection(i) for i in range(max_connections)]  # Cria as conexões
        self.wait_queue = queue.Queue()                            # Fila de espera para requisições

    def get_connection(self):
        """Obtém uma conexão disponível ou aguarda até que uma conexão seja liberada."""
        with self._lock:
            # Verifica todas as conexões para encontrar uma disponível
            for conn in self.connections:
                if not conn.in_use:           # Se a conexão não está em uso
                    conn.in_use = True        # Marca como em uso
                    logging.info(f"Conexão {conn.id} alocada.")  # Log de alocação
                    return conn               # Retorna a conexão disponível
            # Se todas as conexões estão em uso, adiciona a requisição à fila
            logging.info("Todas as conexões estão em uso. Aguardando liberação.")
            waiter = threading.Event()          # Cria um evento de espera
            self.wait_queue.put(waiter)         # Adiciona o evento à fila
            waiter.wait()                       # Aguarda até que a conexão seja liberada
            return self.get_connection()        # Tenta novamente após ser notificado

    def release_connection(self, connection):
        """Libera uma conexão e notifica uma requisição em espera."""
        with self._lock:
            connection.in_use = False           # Marca a conexão como não estando em uso
            logging.info(f"Conexão {connection.id} liberada.")  # Log de liberação
            if not self.wait_queue.empty():      # Verifica se há threads aguardando
                waiter = self.wait_queue.get()   # Remove o próximo evento da fila
                waiter.set()                     # Notifica a thread para tentar obter a conexão

# Função de teste para simular o uso do pool
def simulate_connection_request(pool, request_id):
    logging.info(f"Thread {request_id} solicitando conexão.")  # Log de solicitação
    conn = pool.get_connection()                               # Solicita uma conexão do pool
    logging.info(f"Thread {request_id} usando conexão {conn.id}.")  # Log de uso da conexão
    time.sleep(2)                                              # Simula o tempo de uso da conexão
    pool.release_connection(conn)                              # Libera a conexão após o uso
    logging.info(f"Thread {request_id} liberou conexão {conn.id}.")  # Log de liberação

if __name__ == "__main__":
    pool = DatabaseConnectionPool(max_connections=3)  # Inicializa o pool com limite de 3 conexões

    # Simula múltiplas requisições de conexão com threads
    threads = []
    for i in range(10):                               # Cria 10 threads para simular múltiplas requisições
        thread = threading.Thread(target=simulate_connection_request, args=(pool, i))
        threads.append(thread)                        # Adiciona a thread à lista
        thread.start()                                # Inicia a thread

    # Aguarda todas as threads completarem
    for thread in threads:
        thread.join()                                 # Aguarda o término de cada thread

    logging.info("Teste do pool de conexões concluído.")  # Log de conclusão do teste
