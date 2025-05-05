import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título do app
st.title("Aplicação com Streamlit")

# Texto simples
st.write("Este é um exemplo básico de um aplicativo com Streamlit.")

# Criando um slider interativo
valor = st.slider("Escolha um número", 0, 100, 50)
st.write(f"Você escolheu: {valor}")

# Criando um botão
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")

# Entrada de texto
nome = st.text_input("Digite seu nome:")
if nome:
    st.write(f"Olá, {nome}!")

# Título da aplicação
st.title("Gráfico com Matplotlib no Streamlit")

# Criando os dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Criando a figura do Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y, label="Seno de x", color="blue")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_title("Gráfico de Seno")
ax.legend()

# Exibindo o gráfico no Streamlit
st.pyplot(fig)
