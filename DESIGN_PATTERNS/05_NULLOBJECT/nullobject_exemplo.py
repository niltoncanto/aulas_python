from abc import ABC, abstractmethod
class AbstractOperation(ABC):
    @abstractmethod
    def request(self):
        pass

class RealOperation(AbstractOperation):
    def request(self):
        print("RealOperation: Processando o request.")

class NullOperation(AbstractOperation):
    def request(self):
        # Nenhuma operação é realizada aqui, imitando o comportamento "null"
        print("NullOperation: Nenhuma operação realizada.")

def client_code(operation: AbstractOperation):
    # O código do cliente pode usar a operação sem se preocupar se ela é nula
    operation.request()

class OperationFactory:
    def get_operation(self, type: str) -> AbstractOperation:
        if type == "active":
            return RealOperation()
        elif type == "null":
            return NullOperation()
        elif type is None:
            print("Valor `None` recebido. Retornando NullOperation por padrão.")
            return NullOperation()
        else:
            raise ValueError(f"Tipo de operação inválido: {type}")

if __name__ == "__main__":
    factory = OperationFactory()

    # Caso válido: RealOperation
    operation = factory.get_operation("active")
    operation.request()

    # Caso válido: NullOperation
    operation = factory.get_operation("null")
    operation.request()

    # Caso inválido: None como entrada
    operation = factory.get_operation(None)
    operation.request()

    # Caso inválido: Tipo não suportado
    try:
        operation = factory.get_operation("unsupported")
        operation.request()
    except ValueError as e:
        print(e)





