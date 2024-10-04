// Q1) Crie uma classe Carro com atributos como marca, modelo, e
//ano. Instancie três objetos dessa classe e exiba os detalhes de cada um.

class Main {
    static class Carro {
        private String marca;
        private String modelo;
        private int ano;

        public Carro(String marca, String modelo, int ano) {
            this.marca = marca;
            this.modelo = modelo;
            this.ano = ano;
        }

        public void detalhes() {
            System.out.println("Marca: " + marca + ", Modelo: " + modelo + ", Ano: " + ano);
        }
    }

    public static void main(String[] args) {
        Carro carro1 = new Carro("Hyundai", "HB20x", 2015);
        Carro carro2 = new Carro("Fiat", "Punto", 2012);
        Carro carro3 = new Carro("Ford", "EcoSport", 2019);

        carro1.detalhes();
        carro2.detalhes();
        carro3.detalhes();
    }
}