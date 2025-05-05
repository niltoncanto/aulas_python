import tkinter as tk

def imprime():
    resLabel['text'] = nome.get() + telefone.get()

janela = tk.Tk()
janela.title("Janela teste")
janela.geometry('400x300')

nomeLabel = tk.Label(janela,text="Nome:")
nomeLabel.pack()
nome = tk.Entry(janela)
nome.pack()

telefoneLabel = tk.Label(janela,text="Telefone:")
telefoneLabel.pack()
telefone = tk.Entry(janela)
telefone.pack()

resLabel = tk.Label(janela,text="")
resLabel.pack()

botao = tk.Button(text="Enviar", command=imprime)
botao.pack()

janela.mainloop()


