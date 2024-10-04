// Q3)  Implemente uma classe ContaBancaria com atributos saldo, titular e
// métodos depositar e sacar. Use encapsulamento para proteger o atributo saldo.

public class Main {

    static class ContaBancaria {
        private String titular;
        private double saldo;

        public ContaBancaria(String titular, double saldoInicial) {
            this.titular = titular;
            this.saldo = saldoInicial;
        }

        public double getSaldo() {
            return saldo;
        }

        public void depositar(double valor) {
            if (valor > 0) {
                saldo += valor;
                System.out.printf("Depositados R$%.2f na conta de %s.\n", valor, titular);
            } else {
                System.out.println("Valor inválido para depósito.");
            }
        }

        public void sacar(double valor) {
            if (valor > 0 && valor <= saldo) {
                saldo -= valor;
                System.out.printf("Sacados R$%.2f da conta de %s.\n", valor, titular);
            } else if (valor > saldo) {
                System.out.println("Saldo insuficiente para o saque.");
            } else {
                System.out.println("Valor inválido para saque.");
            }
        }
    }

    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("Luan", 1700.00);

        System.out.printf("Saldo inicial de %s: R$%.2f\n", conta.titular, conta.getSaldo());

        conta.depositar(500.00);
        System.out.printf("Saldo após depósito: R$%.2f\n", conta.getSaldo());

        conta.sacar(300.00);
        System.out.printf("Saldo após saque: R$%.2f\n", conta.getSaldo());

        conta.sacar(2000.00);
        System.out.printf("Saldo após tentativa de saque: R$%.2f\n", conta.getSaldo());
    }
}
