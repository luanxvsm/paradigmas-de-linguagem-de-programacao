interface Imprimivel {
    void imprimir();
}

class Relatorio implements Imprimivel {
    private String conteudo;

    public Relatorio(String conteudo) {
        this.conteudo = conteudo;
    }

    @Override
    public void imprimir() {
        System.out.println("Imprimindo relatório: " + conteudo);
    }
}

class Contrato implements Imprimivel {
    private String detalhes;

    public Contrato(String detalhes) {
        this.detalhes = detalhes;
    }

    @Override
    public void imprimir() {
        System.out.println("Imprimindo contrato: " + detalhes);
    }
}

public class Main {
    public static void main(String[] args) {
        Imprimivel relatorio = new Relatorio("Relatório financeiro");
        Imprimivel contrato = new Contrato("Contrato de prestação de serviços");

        relatorio.imprimir();
        contrato.imprimir();
    }
}
