class Calculadora {
    // Sobrecarga de método: soma de dois inteiros
    public int somar(int a, int b) {
        return a + b; 
    }
    // Sobrecarga de método: soma de três inteiros
    public int somar(int a, int b, int c) {
        return a + b + c; 
    }

    // Sobrecarga de método: soma de dois números de ponto flutuante
    public double somar(double a, double b) {
        return a + b; 
    }
}

public class Main {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        System.out.println(calc.somar(10, 20));           // Saída: 30
        System.out.println(calc.somar(10, 20, 30));       // Saída: 60
        System.out.println(calc.somar(10.5, 20.5));       // Saída: 31.0
    }
}
