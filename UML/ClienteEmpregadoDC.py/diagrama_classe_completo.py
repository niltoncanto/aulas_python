from abc import ABC, abstractmethod
#O Produto pode existir independentemente de qualquer ItemDePedido.
class Produto:
    def __init__(self, codigo, nome, preco):
        self.__codigo = codigo  # Visibilidade privada
        self.__nome = nome  # Visibilidade privada
        self.__preco = preco  # Visibilidade privada

    # Getters para os atributos privados (opcional)
    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

# O ItemDePedido agrega um Produto, mas o Produto não depende do ItemDePedido. 
# Ou seja, o Produto pode existir sem o ItemDePedido.
class ItemDePedido:
    def __init__(self, quantidade, preco, em_estoque, produto):
        self.__quantidade = quantidade  # Visibilidade privada
        self.__preco = preco  # Visibilidade privada
        self.__em_estoque = em_estoque  # Visibilidade privada
        self.produto = produto  # Agregação: Produto é associado, mas pode existir independentemente

    # Métodos para acessar os atributos
    def get_quantidade(self):
        return self.__quantidade

    def get_preco(self):
        return self.__preco

    def is_em_estoque(self):
        return self.__em_estoque

    def get_produto(self):
        return self.produto

# O Pedido "compõe" seus ItensDePedido. 
# Se o Pedido for destruído, todos os ItensDePedido também são destruídos. 
# O Pedido é o "todo", e os ItensDePedido são as "partes".    
class Pedido:
    def __init__(self, codigo, data_recebido, total):
        self.__codigo = codigo  # Visibilidade privada
        self.__data_recebido = data_recebido  # Visibilidade privada
        self.__total = total  # Visibilidade privada
        self.__itens = []  # Composição: Pedido "possui" uma lista de ItensDePedido

    def adicionar_item(self, quantidade, preco, em_estoque, produto):
        # Cria um novo ItemDePedido e adiciona à lista (composição)
        item = ItemDePedido(quantidade, preco, em_estoque, produto)
        self.__itens.append(item)

    def remover_item(self, item):
        # Remove o ItemDePedido da lista
        self.__itens.remove(item)

    def get_itens(self):
        return self.__itens

    def cancelar(self):
        # Quando o pedido é cancelado, os itens também são destruídos
        self.__itens.clear()

    # Métodos para acessar os atributos do pedido
    def get_codigo(self):
        return self.__codigo

    def get_data_recebido(self):
        return self.__data_recebido

    def get_total(self):
        return self.__total

class IPessoa(ABC):
    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_documento(self):
        pass

class Cliente:
    def __init__(self, id, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado):
        self.__id = id  # Visibilidade privada
        self.__nome = nome  # Visibilidade privada
        self.__endereco = endereco  # Visibilidade privada
        self.__data_primeira_compra = data_primeira_compra  # Visibilidade privada
        self.__data_ultima_compra = data_ultima_compra  # Visibilidade privada
        self.__total_comprado = total_comprado  # Visibilidade privada

    def get_nome(self):
        return self.__nome

    # Outros métodos comuns ao Cliente...

class ClientePessoaJuridica(Cliente, IPessoa):
    def __init__(self, id, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado, nome_contato, telefones, cgc, fax):
        super().__init__(id, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado)
        self.__nome_contato = nome_contato  # Visibilidade privada
        self.__telefones = telefones  # Visibilidade privada (Lista de 1 a 10 Strings)
        self.__cgc = cgc  # Visibilidade privada
        self.__fax = fax  # Visibilidade privada (Lista de 1 a 3 Strings)

    def get_documento(self):
        return self.__cgc

class ClientePessoaFisica(Cliente, IPessoa):
    def __init__(self, id, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado, cpf, num_cartao_credito):
        super().__init__(id, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado)
        self.__cpf = cpf  # Visibilidade privada
        self.__num_cartao_credito = num_cartao_credito  # Visibilidade privada

    def get_documento(self):
        return self.__cpf

    def colocar_lista_negra(self):
        pass  # Método público específico de ClientePessoaFisica

class Empregado(IPessoa):
    def __init__(self, nome, cpf, cargo):
        self.__nome = nome  # Visibilidade privada
        self.__cpf = cpf  # Visibilidade privada
        self.__cargo = cargo  # Visibilidade privada

    def get_nome(self):
        return self.__nome

    def get_documento(self):
        return self.__cpf




