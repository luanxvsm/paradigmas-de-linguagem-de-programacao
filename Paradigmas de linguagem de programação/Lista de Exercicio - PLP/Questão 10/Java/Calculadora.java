// Q10) Implemente uma classe Calculadora com métodos somar que aceita diferentes números
// de parâmetros (dois ou três números). Em Golang, use funções com nomes diferentes
// para diferentes quantidades de parâmetros

class CalculadoraBase {
    public int somar(int a, int b) {
        return a + b;
    }
}

public class Calculadora extends CalculadoraBase {
    @Override
    public int somar(int a, int b) {
        return a + b;
    }

    public int somar(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        int resultado1 = calc.somar(5, 10);
        System.out.println("Soma de 5 + 10 = " + resultado1);
        int resultado2 = calc.somar(5, 10, 15);
        System.out.println("Soma de 5 + 10 + 15 = " + resultado2);
    }
}
