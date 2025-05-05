import pytest
from calculadora import StatsCalculator  # Substitua 'your_module' pelo nome do módulo onde a classe StatsCalculator está definida

class TestStatsCalculator:
    def test_mean(self):
        """
        Testa o método mean da classe StatsCalculator.
        """
        calc = StatsCalculator([1, 2, 3, 4, 5])
        assert calc.mean() == 3.0

        calc = StatsCalculator([1])
        assert calc.mean() == 1.0

        calc = StatsCalculator([])
        assert calc.mean() == 0

    def test_median(self):
        """
        Testa o método median da classe StatsCalculator.
        """
        calc = StatsCalculator([1, 2, 3, 4, 5])
        assert calc.median() == 3.0

        calc = StatsCalculator([1, 2, 3, 4])
        assert calc.median() == 2.5

        calc = StatsCalculator([1])
        assert calc.median() == 1.0

        calc = StatsCalculator([])
        assert calc.median() == 0

    def test_std_dev(self):
        """
        Testa o método std_dev da classe StatsCalculator.
        """
        calc = StatsCalculator([1, 2, 3, 4, 5])
        assert calc.std_dev() == pytest.approx(1.41421, 0.00001)

        calc = StatsCalculator([1])
        assert calc.std_dev() == 0

        calc = StatsCalculator([])
        assert calc.std_dev() == 0
