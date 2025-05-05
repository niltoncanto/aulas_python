from abc import ABC, abstractmethod

class ClasseAbstrata(ABC):
    @abstractmethod
    def __init__(self) -> None:
        print("x")

    def fazAlgo():
        print("Y")


objeto = ClasseAbstrata()


