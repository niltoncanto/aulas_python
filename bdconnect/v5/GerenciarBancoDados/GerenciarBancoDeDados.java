package GerenciarBancoDados;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class GerenciarBancoDeDados {
    private Connection conexao; // Declaração de uma variável de conexão.

    public GerenciarBancoDeDados() {
        // Construtor: Aqui você pode inicializar a conexão com o banco de dados.
        conectarBD(); // Chamando o método para estabelecer a conexão com o banco de dados.
    }

    public void conectarBD() {
        try {
            String url = "jdbc:sqlserver://aulas.database.windows.net:1433;databaseName=aulas";
            String usuario = "aluno";
            String senha = "ShuPez@12tZHT";
            conexao = DriverManager.getConnection(url, usuario, senha); // Estabelece a conexão com o banco de dados.
            System.out.println("Conexão estabelecida com sucesso!"); // Exibe uma mensagem de sucesso.
        } catch (SQLException e) {
            System.err.println("Erro ao conectar ao banco de dados:"); // Exibe uma mensagem de erro.
            e.printStackTrace(); // Exibe informações detalhadas sobre o erro.
        }
    }

    public void selectBD(String tabela) {
        String sql = "SELECT * FROM " + tabela;
        try (PreparedStatement stmt = conexao.prepareStatement(sql);
                ResultSet rs = stmt.executeQuery()) {
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") + 
                                   "  nome: " + rs.getString("nome") + 
                                   "  ra: " + rs.getString("ra") +
                                   "  id_curso: " + rs.getString("id_curso") +
                                   "  semestre: " + rs.getString("semestre"));
            }
        } catch (SQLException e) {
            System.err.println("Erro ao executar a consulta:"); // Exibe uma mensagem de erro.
            e.printStackTrace(); // Exibe informações detalhadas sobre o erro.
        }
    }

    public void insertBD(String tabela, String nome, String ra, String id_curso, String semestre) {
        String sql = "INSERT INTO " + tabela + " (nome, ra, id_curso, semestre) VALUES (?, ?, ?, ?)";
        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setString(1, nome);
            stmt.setString(2, ra);
            stmt.setString(3, id_curso);
            stmt.setString(4, semestre);
            
            int linhasAfetadas = stmt.executeUpdate();
            if (linhasAfetadas > 0) {
                System.out.println("Registro inserido com sucesso!"); // Exibe uma mensagem de sucesso.
            } else {
                System.err.println("Nenhum registro inserido."); // Exibe uma mensagem de erro.
            }
        } catch (SQLException e) {
            System.err.println("Erro ao executar a inserção:"); // Exibe uma mensagem de erro.
            e.printStackTrace(); // Exibe informações detalhadas sobre o erro.
        }
    }
    
    public void updateBD(String tabela, int id, String novoNome, String novoRa, String novoIdCurso, String novoSemestre) {
        String sql = "UPDATE " + tabela + " SET nome = ?, ra = ?, id_curso = ?, semestre = ? WHERE id = ?";
        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setString(1, novoNome);
            stmt.setString(2, novoRa);
            stmt.setString(3, novoIdCurso);
            stmt.setString(4, novoSemestre);
            stmt.setLong(5, id);
            
            int linhasAfetadas = stmt.executeUpdate();
            if (linhasAfetadas > 0) {
                System.out.println("Registro atualizado com sucesso!"); // Exibe uma mensagem de sucesso.
            } else {
                System.err.println("Nenhum registro atualizado."); // Exibe uma mensagem de erro.
            }
        } catch (SQLException e) {
            System.err.println("Erro ao executar a atualização:"); // Exibe uma mensagem de erro.
            e.printStackTrace(); // Exibe informações detalhadas sobre o erro.
        }
    }

    public void deleteBD(String tabela, int id) {
        String sql = "DELETE FROM " + tabela + " WHERE id = ?";
        try (PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setInt(1, id);
            
            int linhasAfetadas = stmt.executeUpdate();
            if (linhasAfetadas > 0) {
                System.out.println("Registro excluído com sucesso!"); // Exibe uma mensagem de sucesso.
            } else {
                System.err.println("Nenhum registro excluído."); // Exibe uma mensagem de erro.
            }
        } catch (SQLException e) {
            System.err.println("Erro ao executar a exclusão:"); // Exibe uma mensagem de erro.
            e.printStackTrace(); // Exibe informações detalhadas sobre o erro.
        }
    }
    

    public void fecharConexao() {
        try {
            if (conexao != null && !conexao.isClosed()) {
                conexao.close();
                System.out.println("Conexão fechada com sucesso!"); // Exibe uma mensagem de sucesso.
            }
        } catch (SQLException e) {
            System.err.println("Erro ao fechar a conexão:"); // Exibe uma mensagem de erro.
            e.printStackTrace(); // Exibe informações detalhadas sobre o erro.
        }
    }

    public static void main(String[] args) {
        GerenciarBancoDeDados con = new GerenciarBancoDeDados(); // Crie uma instância da sua classe Conectar
    
        // Teste 1: Verificar a conexão
        if (con != null && con.conexao != null) {
            System.out.println("Teste 1: Conexão estabelecida com sucesso!"); // Exibe uma mensagem de sucesso.
        } else {
            System.err.println("Teste 1: Falha na conexão."); // Exibe uma mensagem de erro.
            return; // Encerra o programa se a conexão falhar
        }
    
        // Teste 2: Listar tabela alunos
        System.out.println("Teste 2: Listando tabela alunos...");
        con.selectBD("alunos");
    
        // Teste 3: Inserir um novo aluno
        System.out.println("Teste 3: Inserindo um novo aluno...");
        con.insertBD("alunos", "Novo Aluno", "RA823457", "1", "3");
    
        // Teste 4: Listar tabela alunos novamente
        System.out.println("Teste 4: Listando tabela alunos após a inserção...");
        con.selectBD("alunos");
    
        // Teste 5: Atualizar o nome do aluno inserido anteriormente
        System.out.println("Teste 5: Atualizando o nome do aluno...");
        con.updateBD("alunos", 1, "Novo Nome Aluno", "RA823457", "1", "3");
    
        // Teste 6: Listar tabela alunos novamente após a atualização
        System.out.println("Teste 6: Listando tabela alunos após a atualização do nome...");
        con.selectBD("alunos");
    
        // Teste 7: Deletar o aluno criado anteriormente
        System.out.println("Teste 7: Deletando o aluno criado anteriormente...");
        con.deleteBD("alunos", 1);
    
        // Teste 8: Fechar a conexão
        con.fecharConexao();
    }
}

/*
PreparedStatement stmt = conexao.prepareStatement(sql)
Esta linha de código está criando um objeto do tipo PreparedStatement chamado stmt usando a conexão com o banco de dados (conexao) para preparar uma consulta SQL ou uma instrução SQL parametrizada.
Aqui está o que cada parte dessa linha faz:

PreparedStatement: PreparedStatement é uma interface no Java que estende a interface Statement. Ele é usado para executar instruções SQL pré-compiladas com parâmetros. O uso de PreparedStatement é preferido quando você precisa executar a mesma instrução SQL várias vezes com valores diferentes ou quando deseja evitar ataques de injeção SQL, pois ele ajuda a proteger contra esses tipos de ataques.

stmt: É o nome da variável que estamos declarando para armazenar a referência ao objeto PreparedStatement que será criado. Você pode escolher qualquer nome de variável válido.

conexao.prepareStatement(sql): Esta parte da linha cria o objeto PreparedStatement. Aqui está o que está acontecendo:

conexao: É a conexão com o banco de dados que foi estabelecida anteriormente no código.
prepareStatement(sql): Este é um método da classe Connection. Ele prepara uma instrução SQL para execução e aceita uma string contendo a instrução SQL como argumento. Neste caso, a instrução SQL está armazenada na variável sql.
Após essa linha de código, você pode configurar os parâmetros da instrução SQL (se houver algum) usando métodos como setString(), setInt(), etc., e então você pode executar a instrução SQL usando métodos como executeQuery() (para consultas) ou executeUpdate() (para instruções de atualização, inserção ou exclusão).

Em resumo, a linha em questão cria um objeto PreparedStatement que está pronto para executar uma instrução SQL preparada usando a conexão com o banco de dados estabelecida anteriormente. Isso é fundamental para executar consultas seguras e eficientes em um banco de dados Java.
 */
