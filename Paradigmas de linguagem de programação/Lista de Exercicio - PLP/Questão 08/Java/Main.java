import java.util.ArrayList;
import java.util.List;

class Empregado {
    private String nome;
    private String cargo;
    private double salario;

    public Empregado(String nome, String cargo, double salario) {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }

    public String getCargo() {
        return cargo;
    }

    public double getSalario() {
        return salario;
    }
}

class Empresa {
    private List<Empregado> empregados = new ArrayList<>();

    public void adicionarEmpregado(Empregado empregado) {
        empregados.add(empregado);
    }

    public List<Empregado> getEmpregados() {
        return empregados;
    }
}

public class Main {
    public static void main(String[] args) {
        Empresa empresa = new Empresa();
        empresa.adicionarEmpregado(new Empregado("João", "Desenvolvedor", 3000.00));
        empresa.adicionarEmpregado(new Empregado("Maria", "Gerente", 5000.00));

        for (Empregado e : empresa.getEmpregados()) {
            System.out.println(e.getNome() + " - " + e.getCargo() + " - " + e.getSalario());
        }
    }
}
