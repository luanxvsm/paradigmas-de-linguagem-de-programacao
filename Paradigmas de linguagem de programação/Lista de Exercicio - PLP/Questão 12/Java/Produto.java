// Q12) Em Python,
// sobrecarregue o operador + para somar dois objetos Produto baseados no preço. Em Java
// e Golang, crie métodos que permitam essa funcionalidade.

class Produto {
    private String nome;
    private double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public Produto somar(Produto outro) {
        String nomeCombinado = this.nome + " & " + outro.nome;
        double precoCombinado = this.preco + outro.preco;
        return new Produto(nomeCombinado, precoCombinado);
    }

    @Override
    public String toString() {
        return "Produto: " + nome + ", Preço: " + preco;
    }

    public static void main(String[] args) {
        Produto produto1 = new Produto("Produto A", 50);
        Produto produto2 = new Produto("Produto B", 30);

        Produto produtoSoma = produto1.somar(produto2);
        System.out.println(produtoSoma);
    }
}