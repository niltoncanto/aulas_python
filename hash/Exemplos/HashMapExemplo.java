import java.util.Map;
import java.util.HashMap;

public class HashMapExemplo {
    public static void main(String[] args) {
        Map<String, String> mapa = new HashMap<>();
        mapa.put("nome", "Mariana");
        mapa.put("idade","25");

        System.out.println("nome -> " + mapa.get("nome"));   // nome → 1
    }
}