class GerenciadorDePersistencia:
    @staticmethod
    def salvar_livro(livro):
        try:
            with open('livros.txt', 'a', encoding='utf-8') as f:
                f.write(livro.to_string() + "\n")
        except IOError as e:
            return e

    @staticmethod
    def carregar_livros():
        livros = []
        try:
            with open('livros.txt', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(';')
                    if partes[4] == "Padrao":
                        livro = LivroPadrao(partes[0], partes[1], partes[2])
                    elif partes[4] == "Referencia":
                        livro = LivroReferencia(partes[0], partes[1], partes[2], partes[5])
                    livro.status = Status[partes[3]]
                    livros.append(livro)
        except FileNotFoundError:
            print("Arquivo de livros não encontrado.")
        return livros

    @staticmethod
    def salvar_usuario(usuario):
        with open('usuarios.txt', 'a', encoding='utf-8') as f:
                print(usuario.to_string())
                f.write(usuario.to_string()+ "\n")

    @staticmethod
    def carregar_usuarios():
        usuarios = []
        try:
            with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    nome, ID = linha.strip().split(';')
                    usuarios.append(Usuario(nome, ID))
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado.")
        return usuarios
