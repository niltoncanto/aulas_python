package ExTestes.Gbd;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.*;

public class GerenciarBancoDeDados {
    private Connection conexao;

    public GerenciarBancoDeDados(){
        conectarBD();
    }

    public void conectarBD(){
        try {
            String url = "jdbc:sqlserver://aulas.database.windows.net:1433;databaseName=aulas";
            String usuario = "aluno";
            String senha = "ShuPez@12tZHT";
            conexao = DriverManager.getConnection(url,usuario,senha);
            System.out.println("Conexão estabelecida com sucesso!");
        } catch (SQLException e){
            System.err.println("Erro ao conectar BD!");
            e.printStackTrace();
        }
    }

    public void selectBD(String tabela){
        String sql = "SELECT * FROM " + tabela;
        try(PreparedStatement stmt = conexao.prepareStatement(sql)) {
            ResultSet rs = stmt.executeQuery();
            while(rs.next()){
                System.out.println("id: "+rs.getInt("id")+
                "nome: " + rs.getString("nome")+
                "ra: " + rs.getString("ra")+ 
                "id_curso: " + rs.getInt("id_curso")+
                "semestre: " + rs.getInt("semestre")
                );
            }
        } catch (SQLException e){
            System.err.println("Erro ao selecionar tabela!");
            e.printStackTrace();        
        }
    }

    public void insertBD(String tabela, String nome, String ra){
        String sql = "INSERT INTO " + tabela + " (nome, ra)  VALUES (?,?)";
        try(PreparedStatement stmt = conexao.prepareStatement(sql)){
            stmt.setString(1,nome);
            stmt.setString(2,ra);
            int linha = stmt.executeUpdate();
            System.out.println("registro inserido com sucesso");
        } catch (SQLException e) {
            System.err.println("erro ao inserir registro");
        }
    }

    public void updateBD(String tabela, String nome, String ra, int id_curso, int id){
        String sql = "UPDATE " + tabela + " SET nome = ?, ra = ?, id_curso = ? WHERE id = ?";
        try (PreparedStatement stmt = conexao.prepareStatement(sql)){
            stmt.setString(1,nome);
            stmt.setString(2,ra);
            stmt.setInt(3, id_curso);
            stmt.setInt(4,id);

            int linha = stmt.executeUpdate();
            System.out.println("Registro alterado com sucesso");
        }catch (SQLException e){
            System.err.println("erro ao atualizar registro.");
        }
    }

    public void deleteBD(String tabela, int id){
        String sql = "DELETE FROM " + tabela + "WHERE id = ?";
        try(PreparedStatement stmt = conexao.prepareStatement(sql)){
            stmt.setInt(1,id);
            int linha = stmt.executeUpdate();
            if(linha>0){
                System.out.println("registro excluído com sucesso");
            }else{
                System.out.println("nenhum registro excluído com sucesso");
            }
        }catch (SQLException e){
            System.err.println("erro ao excluir registro.");
        }
    }

    public void fecharConexao(){
        try{
            if(conexao != null && !conexao.isClosed()){
                conexao.close();
                System.out.println("Conexão finalizada!");
            }
        }catch (SQLException e){
            System.err.println("Erro ao fechar conexão!");
        }
    }

    public static void main(String[] args){
        GerenciarBancoDeDados con = new GerenciarBancoDeDados();
        //Teste 1 verificar conexão
        if(con!=null && con.conexao !=null){
            System.out.println("Teste 1: conexão estabelecida!");
        }else{
            System.out.println("Teste 1: Falha de conexão");
        }

        //teste2 listar tabela
        System.out.println("Teste 2: Listando tabela alunos ...");
        con.selectBD("alunos");

        //teste3 inserir na tabela
        System.out.println("Teste 3: Inserindo um novo aluno ...");
        con.insertBD("alunos", "João da Silva", "0999999");

        //teste2 listar tabela
        System.out.println("Teste 2: Listando tabela alunos ...");
        con.selectBD("alunos");

        //teste 4 update aluno
        System.out.println("Teste 4: atualizando um novo aluno ...");
        con.updateBD("alunos", "João Pedro", "0999999", 4, 15);

        //teste2 listar tabela
        System.out.println("Teste 2: Listando tabela alunos ...");
        con.selectBD("alunos");

        //teste5 excluir aluno da tabela
        System.out.println("Teste 2: Excluir tabela alunos ...");
        con.deleteBD("alunos",20);

    }
}
