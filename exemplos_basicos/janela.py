import tkinter as tk

def on_submit():
    label_resultado['text'] = f'Olá, {entry_nome.get()}!'

# Criar a janela principal
janela = tk.Tk()
janela.title("Minha Pequena Tela")

# Configurar tamanho da janela
janela.geometry('300x200')  # Largura x Altura

# Adicionar um campo de entrada (entry)
entry_nome = tk.Entry(janela)
entry_nome.pack(pady=10)  # Adiciona um pouco de espaço vertical

# Adicionar um botão que, quando pressionado, executa uma função
botao_submit = tk.Button(janela, text="Cumprimente-me", command=on_submit)
botao_submit.pack()

# Adicionar uma etiqueta para mostrar o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

# Iniciar o loop principal
janela.mainloop()
