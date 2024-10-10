class Motor {
    private int potencia;
    public Motor(int potencia) {
        this.potencia = potencia;
    }
    public int getPotencia() {
        return potencia;
    }
}

class Carro {
    private Motor motor;
    public Carro(Motor motor) {
        this.motor = motor;
    }
    public Motor getMotor() {
        return motor;
    }
}

public class Main {
    public static void main(String[] args) {
        Motor motor = new Motor(310);
        Carro carro = new Carro(motor);
        System.out.println("Potência do motor: " + carro.getMotor().getPotencia());
    }
}
