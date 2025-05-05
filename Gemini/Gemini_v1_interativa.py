import google.generativeai as genai  # Importa a biblioteca do Google para interagir com modelos generativos de IA.

class GeminiGeradorDeTextos:  # Define uma classe chamada 'GeminiGeradorDeTextos'.
    def __init__(self):  # Método construtor da classe, que é chamado quando um objeto da classe é criado.
        # Define a chave da API do Google que será usada para autenticação.
        GOOGLE_API_KEY = 'AIzaSyDLQClyg_QSS_h5VTl9ssvF3QO5gP9eEx4'
        # Configura a biblioteca genai com a chave da API.
        genai.configure(api_key=GOOGLE_API_KEY)

    def gerador_de_textos(self, prompt):  # Define um método que recebe um prompt e gera um texto a partir dele.
        # Cria um objeto do modelo 'gemini-1.5-flash' para geração de conteúdo.
        model = genai.GenerativeModel("gemini-1.5-flash")
        # Gera o conteúdo baseado no prompt fornecido e armazena a resposta.
        response = model.generate_content(prompt)
        # Imprime o texto gerado pelo modelo.
        print(response.text)

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente.
    gemini = GeminiGeradorDeTextos()  # Cria uma instância da classe 'GeminiGeradorDeTextos'.
    while True:  # Inicia um loop infinito para permitir múltiplas interações.
        # Solicita ao usuário que digite uma mensagem para o modelo, ou a palavra 'sair' para encerrar.
        prompt = input("Mensagem para o Gemini (ou digite 'sair' para encerrar): ")
        if prompt.lower() == 'sair':  # Verifica se o usuário digitou 'sair' (case insensitive).
            print("Conversa encerrada.")  # Imprime uma mensagem de encerramento.
            break  # Sai do loop, encerrando o programa.
        gemini.gerador_de_textos(prompt)  # Chama o método 'gerador_de_textos' com o prompt fornecido pelo usuário.
