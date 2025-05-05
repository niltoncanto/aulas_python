class Pagina:
    def __init__(self, numero, conteudo):
        self.numero = numero
        self.conteudo = conteudo
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.paginas = []
    def adicionar_pagina(self, pagina):
        self.paginas.append(pagina)
    def obter_paginas(self):
        return [p.numero for p in self.paginas]
l = Livro("Python 101")
p1 = Pagina(1, "Introdução")
p2 = Pagina(2, "Estruturas de Dados")
l.adicionar_pagina(p1)
l.adicionar_pagina(p2)
print(l.titulo)  # Output: Python 101
print(l.obter_paginas())  # Output: [1, 2]