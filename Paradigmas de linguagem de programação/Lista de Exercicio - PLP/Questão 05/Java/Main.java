interface Animal {
    String som();
}

class Vaca implements Animal {
    public String som() {
        return "Vaca: Muuuu";
    }
}

class Cabra implements Animal {
    public String som() {
        return "Cabra: Béééé";
    }
}

public class Main {
    public static void fazerSomAnimais(Animal[] animais) {
        for (Animal animal : animais) {
            System.out.println(animal.som());
        }
    }

    public static void main(String[] args) {
        Animal[] animais = {new Vaca(), new Cabra()};
        fazerSomAnimais(animais);
    }
}
