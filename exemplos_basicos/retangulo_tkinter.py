import tkinter as tk

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, ponto_inferior_esquerdo, largura, altura):
        self.ponto_inferior_esquerdo = ponto_inferior_esquerdo
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inferior_esquerdo.x + self.largura / 2
        centro_y = self.ponto_inferior_esquerdo.y + self.altura / 2
        return Ponto(centro_x, centro_y)

# Interface Gráfica
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.retangulo = None

    def create_widgets(self):
        self.lbl_x = tk.Label(self, text="X do vértice inferior esquerdo:")
        self.lbl_x.pack(pady=3)

        self.entry_x = tk.Entry(self)
        self.entry_x.pack(pady=3)

        self.lbl_y = tk.Label(self, text="Y do vértice inferior esquerdo:")
        self.lbl_y.pack(pady=3)

        self.entry_y = tk.Entry(self)
        self.entry_y.pack(pady=3)

        self.lbl_largura = tk.Label(self, text="Largura do retângulo:")
        self.lbl_largura.pack(pady=3)

        self.entry_largura = tk.Entry(self)
        self.entry_largura.pack(pady=3)

        self.lbl_altura = tk.Label(self, text="Altura do retângulo:")
        self.lbl_altura.pack(pady=3)

        self.entry_altura = tk.Entry(self)
        self.entry_altura.pack(pady=3)

        self.btn_criar = tk.Button(self, text="Criar Retângulo", command=self.criar_retangulo)
        self.btn_criar.pack(pady=3)

        self.btn_centro = tk.Button(self, text="Imprimir Centro", command=self.imprimir_centro)
        self.btn_centro.pack(pady=3)

        self.resultado = tk.Label(self, text="")
        self.resultado.pack(pady=3)

    def criar_retangulo(self):
        x = float(self.entry_x.get())
        y = float(self.entry_y.get())
        largura = float(self.entry_largura.get())
        altura = float(self.entry_altura.get())
        self.retangulo = Retangulo(Ponto(x, y), largura, altura)
        self.resultado['text'] = "Retângulo criado!"

    def imprimir_centro(self):
        if self.retangulo:
            centro = self.retangulo.encontrar_centro()
            self.resultado['text'] = f"Centro: ({centro.x}, {centro.y})"
        else:
            self.resultado['text'] = "Retângulo não existe, crie primeiro o retângulo."


root = tk.Tk()
root.title("Retângulo")
app = Application(master=root)
app.mainloop()
