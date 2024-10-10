class Main {
    static class Carro {
        private String marca;
        private String modelo;
        private int ano;
        private int velocidade;

        public Carro(String marca, String modelo, int ano) {
            this.marca = marca;
            this.modelo = modelo;
            this.ano = ano;
            this.velocidade = 0;  
        }

        public void detalhes() {
            System.out.println("Marca: " + marca + ", Modelo: " + modelo + ", Ano: " + ano);
        }

        public void acelerar(int incremento) {
            velocidade += incremento;
            System.out.println(modelo + " acelerou para " + velocidade + " km/h.");
        }

        public void frear(int decremento) {
            velocidade -= decremento;
            if (velocidade < 0) {
                velocidade = 0; 
            }
            System.out.println(modelo + " freou para " + velocidade + " km/h.");
        }

        public void exibirVelocidade() {
            System.out.println("A velocidade atual do " + modelo + " é " + velocidade + " km/h.");
        }
    }

    public static void main(String[] args) {
        Carro carro1 = new Carro("Hyundai", "HB20x", 2015);
        Carro carro2 = new Carro("Fiat", "Punto", 2012);
        Carro carro3 = new Carro("Ford", "EcoSport", 2019);
 
        carro1.detalhes();
        carro2.detalhes();
        carro3.detalhes();

        carro1.acelerar(30);
        carro1.exibirVelocidade();
        carro1.frear(10);
        carro1.exibirVelocidade();

        carro2.acelerar(50);
        carro2.exibirVelocidade();
        carro2.frear(20);
        carro2.exibirVelocidade();

        carro3.acelerar(40);
        carro3.exibirVelocidade();
        carro3.frear(40);
        carro3.exibirVelocidade();
    }
}
