import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Minha Primeira Interface Gráfica")

# Definir dimensões da janela
root.geometry("400x200")



def on_button_click():
    label.config(text="Olá, Tkinter!")

# Criar um rótulo
label = tk.Label(root, text="Bem-vindo ao Tkinter")
label.pack(pady=10)  # Posicionar o rótulo na janela

# Criar um botão
button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack(pady=5)  # Posicionar o botão na janela


def item_selecionado():
    # Obter o índice do item selecionado
    indice = listbox.curselection()
    # Obter o item selecionado usando o índice
    item_selecionado = listbox.get(indice)
    label_selecao.config(text=f"Selecionado: {item_selecionado}")

# Criar a janela principal

# Criar um Listbox
listbox = tk.Listbox(root)
listbox.pack(pady=15)

# Adicionar alguns itens ao Listbox
itens = ["Item 1", "Item 2", "Item 3", "Item 4"]
for item in itens:
    listbox.insert(tk.END, item)

# Botão para obter o item selecionado
botao_selecao = tk.Button(root, text="Selecionar", command=item_selecionado)
botao_selecao.pack()

# Label para mostrar o item selecionado
label_selecao = tk.Label(root, text="Selecionado: ")
label_selecao.pack()


# Iniciar o loop de eventos
root.mainloop()