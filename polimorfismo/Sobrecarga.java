class Calculadora {
    public int somar(int a, int b) {
        return a + b;
    }

    public double somar(double a, double b) {
        return a + b;
    }

    public int somar(int a, int b, int c) {
        return a + b + c;
    }
}

public class Sobrecarga {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        System.out.println(calc.somar(4, 5));
        System.out.println(calc.somar(4, 5, 7));
        System.out.println(calc.somar(4.5, 8.9));
    }
}
