import tkinter as tk
from tkinter import messagebox

def attempt_login():
    username = entry_username.get()
    password = entry_password.get()
    # Aqui você adicionaria a lógica de verificação das credenciais no banco de dados
    # Por simplicidade, vamos assumir que o usuário "admin" com senha "1234" é válido
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        # Redirecionamento para a janela principal após o login
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha inválidos.")

app = tk.Tk()
app.title("Login - Sistema de Gerenciamento de Chamados do ERP")

tk.Label(app, text="Nome de Usuário:").pack()
entry_username = tk.Entry(app)
entry_username.pack()

tk.Label(app, text="Senha:").pack()
entry_password = tk.Entry(app, show="*")
entry_password.pack()

tk.Button(app, text="Login", command=attempt_login).pack()

app.mainloop()