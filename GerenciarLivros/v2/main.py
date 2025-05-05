from livroPadrao import LivroPadrao
from livroReferencia import LivroReferencia
from livro import Tema
from usuario import Usuario
from bibliotecario import Bibliotecario
def main():
    '''try:
        livro1 = Livro("ayx","Joao",23223)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    else:
        print("nenhuma excecao foi lançada")
    finally:
        print("este bloco sempre será executado independente de haver ou não lançamento de excecao")'''
    
    #livro1 = LivroPadrao('xyx','joao',12222222222)
    #livro2 = LivroReferencia('xyx','Pedro',1222223332,Tema.FISICA)
    #print(usuario.fazerReserva(livro1))
    #print(usuario.fazerReserva(livro2))
    #print(usuario.fazerDevolucao(livro1))

    usuario1 = Usuario(333,"Maria")
    usuario2 = Usuario("João", "001")
    bibliotecario = Bibliotecario('livros.txt')
    livro1 = LivroPadrao('xyx','joao',12345)
    livro2 = LivroReferencia('yyy','Pedro',54321,Tema.FISICA)
    bibliotecario.adicionar_livro(livro1)
    bibliotecario.adicionar_livro(livro2)
    resp1 = bibliotecario.emprestar_livro("12345", usuario1)
    resp2 = bibliotecario.emprestar_livro("54321", usuario2)
    print(resp1,resp2)

if __name__=="__main__":
    main()