import math

class StatsCalculator:
    def __init__(self, data):
        """
        Inicializa a calculadora de estatísticas com uma lista de dados.
        
        :param data: Lista de números
        """
        self.data = data

    def mean(self):
        """
        Calcula a média dos dados.
        
        :return: Média dos dados
        """
        if len(self.data) == 0:
            return 0
        return sum(self.data) / len(self.data)

    def median(self):
        """
        Calcula a mediana dos dados.
        
        :return: Mediana dos dados
        """
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        
        if n == 0:
            return 0
        
        middle = n // 2
        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]

    def std_dev(self):
        """
        Calcula o desvio padrão dos dados.
        
        :return: Desvio padrão dos dados
        """
        n = len(self.data)
        if n == 0:
            return 0
        
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / n
        return math.sqrt(variance)

# Exemplo de uso
calc = StatsCalculator([1, 2, 3, 4, 5])
print("Média:", calc.mean())
print("Mediana:", calc.median())
print("Desvio Padrão:", calc.std_dev())
