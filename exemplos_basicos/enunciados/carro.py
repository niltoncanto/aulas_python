'''
Objetivo: criar e manipular uma classe Carro que represente as características e comportamentos básicos de um carro.

Parte 1: Declaração da Classe e Atributos
1. Crie uma classe chamada Carro.
2. Declare os seguintes atributos privados:
   - `marca`: String que armazena a marca do carro.
   - `modelo`: String que armazena o modelo do carro.
   - `ano`: Inteiro que armazena o ano do carro.
   - `ligado`: Booleano que indica se o carro está ligado ou desligado.

Parte 2: Construtor
1. Crie um construtor que aceite os parâmetros `marca`, `modelo` e `ano`.
   - Inicialize os atributos com os valores fornecidos.
   - Inicialize o atributo `ligado` como `false`, já que o carro começa desligado.

Parte 3: Métodos
1. Crie um método `ligar` sem parâmetros:
   - Atribua o valor verdadeiro ao atributo `ligado`.
   - Mostre a mensagem "Carro ligado!".
2. Crie um método `desligar` sem parâmetros:
   - Atribua o valor falso ao atributo `ligado`.
   - Mostre a mensagem "Carro desligado!".
3. Crie um método `mostrarInfo` sem parâmetros:
   - Mostre as informações do carro, incluindo a marca, o modelo, o ano e se está ligado ou não.

Parte 4:
Demonstração da classe:
   - Instancie um objeto da classe Carro com os valores "Ford", "Fiesta", 2020.
   - Chame o método `mostrarInfo` para mostrar as informações iniciais do carro.
   - Chame o método `ligar` para ligar o carro e depois chame `mostrarInfo` novamente.
   - Chame o método `desligar` para desligar o carro e depois chame `mostrarInfo` mais uma vez.
'''
