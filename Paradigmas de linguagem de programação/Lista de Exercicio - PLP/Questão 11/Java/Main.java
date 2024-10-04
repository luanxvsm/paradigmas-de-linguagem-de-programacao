// Q11) Crie uma classe abstrata Funcionario com um método abstrato
// calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
// implementam calcularSalario de formas distintas

abstract class Funcionario {

    public abstract double calcularSalario();
}

class FuncionarioHorista extends Funcionario {
    private int horasTrabalhadas;
    private double valorPorHora;

    public FuncionarioHorista(int horasTrabalhadas, double valorPorHora) {
        this.horasTrabalhadas = horasTrabalhadas;
        this.valorPorHora = valorPorHora;
    }

    @Override
    public double calcularSalario() {
        return horasTrabalhadas * valorPorHora;
    }
}

class FuncionarioAssalariado extends Funcionario {
    private double salarioFixo;

    public FuncionarioAssalariado(double salarioFixo) {
        this.salarioFixo = salarioFixo;
    }

    @Override
    public double calcularSalario() {
        return salarioFixo;
    }
}

public class Main {
    public static void main(String[] args) {
        FuncionarioHorista horista = new FuncionarioHorista(160, 25);
        FuncionarioAssalariado assalariado = new FuncionarioAssalariado(3000);

        System.out.println("Salário do funcionário horista: " + horista.calcularSalario());
        System.out.println("Salário do funcionário assalariado: " + assalariado.calcularSalario());
    }
}