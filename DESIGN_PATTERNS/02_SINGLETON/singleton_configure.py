import json
class ConfigManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.load_configurations()
        return cls._instance
    def load_configurations(self):
        with open('config.json', 'r') as file:
            self.config_data = json.load(file)

    def get_config(self, key):
        return self.config_data.get(key, "Configuração não encontrada")
if __name__ == "__main__":
    config_manager = ConfigManager()
    print("URL do Banco de Dados:", config_manager.get_config("database_url"))
    print("Modo Debug:", config_manager.get_config("debug_mode"))
    print("Máximo de Conexões:", config_manager.get_config("max_connections"))
    print("API Key:", config_manager.get_config("api_key"))
    print("Serviço de Email - SMTP Server:", config_manager.get_config("email_service")['smtp_server'])
'''
    {
    "database_url": "http://localhost:5432/meubanco",
    "debug_mode": true,
    "max_connections": 10,
    "api_key": "12345-abcde-67890-fghij",
    "email_service": {
        "smtp_server": "smtp.exemplo.com",
        "smtp_port": 587,
        "use_tls": true
    }
}
'''

