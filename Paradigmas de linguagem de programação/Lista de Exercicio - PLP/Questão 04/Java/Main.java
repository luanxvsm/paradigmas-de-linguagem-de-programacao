interface Animal {
    String som();
}

class Cachorro implements Animal {
    @Override
    public String som() {
        return "Cachorro: AuAu";
    }
}

class Gato implements Animal {
    @Override
    public String som() {
        return "Gato: Miau";
    }
}

public class Main {
    public static void fazerSom(Animal animal) {
        System.out.println(animal.som());
    }

    public static void main(String[] args) {
        Cachorro cachorro = new Cachorro();
        Gato gato = new Gato();

        fazerSom(cachorro);
        fazerSom(gato);
    }
}
