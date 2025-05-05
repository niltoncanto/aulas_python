import datetime
class LogManager:
    __instance = None
    @staticmethod
    def getInstance():
        if LogManager.__instance is None:
            LogManager()
        return LogManager.__instance
    def __init__(self):
        if LogManager.__instance != None:
            raise Exception("Esta classe é um Singleton!")
        else:
            LogManager.__instance = self
    def configure(self, log_to_file, log_file):
        """ Configura o destino do log. """
        self.log_to_file = log_to_file
        self.log_file = log_file
    def log(self, message, level="INFO"):
        """ Registra uma mensagem de log. """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {level}: {message}\n"
        if self.log_to_file:
            with open(self.log_file, 'a') as f:
                f.write(log_message)
        else:
            print(log_message)
# Teste do LogManager
if __name__ == "__main__":
    logger = LogManager.getInstance()
    # Configurando o logger para registrar em arquivo
    logger.configure(log_to_file=True, log_file="app.log")
    # Registrando diferentes tipos de mensagens
    logger.log("Este é um log de informação")
    logger.log("Este é um log de aviso", level="WARNING")
    logger.log("Este é um log de erro", level="ERROR")
