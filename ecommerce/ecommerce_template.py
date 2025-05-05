import uuid

class Pessoa:
    """ Representa uma pessoa com atributos básicos. nome, cpf, email"""
    # construtor da classe

class Cliente:
    """ Representa um cliente do e-commerce, associado a uma pessoa. atributos: pessoa, id_cliente"""
    # construtor da classe utilize a função uuid.uuid4() para gerar um identificador único 
    # exemplo: self.id_cliente = str(uuid.uuid4())

class Produto:
    """ Representa um produto disponível para venda. atributos: nome, preco, estoque"""
    # construtor da classe  

class ItemPedido:
    """ Representa um item dentro de um pedido. Contém um produto e uma quantidade. atributos: produto, quantidade"""
    # construtor da classe

    # método calcular_total

class Pedido:
    """ Representa um pedido realizado por um cliente. Contém o cliente e uma lista de itens. atrubutos: cliente, itens"""
    # construtor da classe
    # método adicionar_item recebe produto e quantidade
    # método calcular_total retorna a soma dos totais dos itens


class Menu:
    """ Gerencia o e-commerce, permitindo o cadastro de clientes, produtos e pedidos. atributos: clientes, produtos, pedidos"""
    # construtor da classe
    # método cadastrar_cliente recebe nome, cpf, email
    # método cadastrar_produto recebe nome, preco, estoque
    # método criar_pedido recebe cpf do cliente
    # método listar_pedidos retorna os pedidos
    # método exibir_menu exibe o menu e executa as opções escolhidas

if __name__ == "__main__":
    menu = Menu()
    menu.exibir_menu()
