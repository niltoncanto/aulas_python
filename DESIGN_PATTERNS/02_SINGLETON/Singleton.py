import json

class ConfigManager:
    # Atributo privado estático para armazenar a instância
    __instance = None

    @staticmethod
    def getInstance():
        """ Método estático de acesso à instância. """
        if ConfigManager.__instance == None:
            ConfigManager()
        return ConfigManager.__instance

    def __init__(self):
        """ Construtor privado. """
        if ConfigManager.__instance != None:
            raise Exception("Esta classe é um Singleton!")
        else:
            ConfigManager.__instance = self
            self.config = {}
            self.load_config()

    def load_config(self):
        """ Carrega as configurações do arquivo. """
        try:
            with open('config.json', 'r') as config_file:
                self.config = json.load(config_file)
        except FileNotFoundError:
            print("Arquivo de configuração não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")

    def get_config(self, key):
        """ Retorna uma configuração específica pelo nome. """
        return self.config.get(key, None)

# Demonstração de uso
if __name__ == "__main__":
    # Obtendo a instância do Singleton
    config_manager = ConfigManager.getInstance()

    # Acessando configurações específicas
    print("URL do Banco de Dados:", config_manager.get_config("database_url"))
    print("Modo de Depuração:", config_manager.get_config("debug_mode"))
