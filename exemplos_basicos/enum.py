#classe enum
from enum import Enum
class DiaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5

print(DiaSemana.SEGUNDA.value)