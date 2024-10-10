import java.util.ArrayList;
import java.util.List;

class Professor {
    private String nome;
    private List<Escola> escolas = new ArrayList<>();

    public Professor(String nome) {
        this.nome = nome;
    }

    public void adicionarEscola(Escola escola) {
        escolas.add(escola);
    }

    public List<Escola> getEscolas() {
        return escolas;
    }

    public String getNome() {
        return nome;
    }
}

class Escola {
    private String nome;
    private List<Professor> professores = new ArrayList<>();

    public Escola(String nome) {
        this.nome = nome;
    }

    public void adicionarProfessor(Professor professor) {
        professores.add(professor);
        professor.adicionarEscola(this);
    }

    public List<Professor> getProfessores() {
        return professores;
    }

    public String getNome() {
        return nome;
    }
}

public class Main {
    public static void main(String[] args) {
        Escola escola1 = new Escola("Escola A");
        Escola escola2 = new Escola("Escola B");

        Professor professor1 = new Professor("Professor X");
        Professor professor2 = new Professor("Professor Y");

        escola1.adicionarProfessor(professor1);
        escola2.adicionarProfessor(professor1);
        escola1.adicionarProfessor(professor2);

        System.out.println(professor1.getNome() + " leciona em: " + professor1.getEscolas().get(0).getNome() + " e " + professor1.getEscolas().get(1).getNome());
        System.out.println(escola1.getNome() + " tem os professores: " + escola1.getProfessores().get(0).getNome() + " e " + escola1.getProfessores().get(1).getNome());
    }
}
