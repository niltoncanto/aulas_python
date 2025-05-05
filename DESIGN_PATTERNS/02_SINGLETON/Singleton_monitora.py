class StateMonitor:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StateMonitor, cls).__new__(cls)
            cls._instance.states = {}
        return cls._instance

    def update_state(self, key, value):
        self.states[key] = value

    def get_state(self, key):
        return self.states.get(key, "Estado não encontrado")

# Testando a classe Singleton
if __name__ == "__main__":
    monitor = StateMonitor()
    monitor.update_state("health", "good")
    monitor.update_state("active_users", 120)

    print("Saúde do Sistema:", monitor.get_state("health"))
    print("Usuários Ativos:", monitor.get_state("active_users"))
