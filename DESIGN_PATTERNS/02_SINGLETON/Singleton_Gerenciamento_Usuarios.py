class UserSettings:
    _instance = None  # Armazena a única instância da classe
    
    def __new__(cls):
        """Garante que apenas uma instância da classe seja criada."""
        if cls._instance is None:
            cls._instance = super(UserSettings, cls).__new__(cls)
            # Inicializa os atributos de configuração na primeira vez que a instância é criada
            cls._instance.tema = "claro"
            cls._instance.tamanho_fonte = 12
            cls._instance.notificacoes = True
        return cls._instance

    def definir_tema(self, tema):
        """Define o tema do usuário."""
        self.tema = tema

    def definir_tamanho_fonte(self, tamanho):
        """Define o tamanho da fonte."""
        self.tamanho_fonte = tamanho

    def definir_notificacoes(self, status):
        """Define o status de notificações."""
        self.notificacoes = status

    def mostrar_configuracoes(self):
        """Exibe as configurações atuais do usuário."""
        return f"Tema: {self.tema}, Tamanho da Fonte: {self.tamanho_fonte}, Notificações: {self.notificacoes}"

# Teste do Singleton
if __name__ == "__main__":
    # Cria a primeira instância de UserSettings
    config1 = UserSettings()
    print(config1.mostrar_configuracoes())  # Exibe as configurações padrão
    
    # Modifica as configurações através da primeira instância
    config1.definir_tema("escuro")
    config1.definir_tamanho_fonte(14)
    config1.definir_notificacoes(False)
    
    # Cria uma segunda "instância" de UserSettings e verifica as configurações
    config2 = UserSettings()
    print(config2.mostrar_configuracoes())  # Deve mostrar as mesmas configurações, pois é a mesma instância
    
    # Verificação final de que config1 e config2 são o mesmo objeto
    print("config1 e config2 são o mesmo objeto?", config1 is config2)
