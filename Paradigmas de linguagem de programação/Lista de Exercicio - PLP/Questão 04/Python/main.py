class Animal:
    def som(self):
        raise NotImplementedError()

class Cachorro(Animal):
    def som(self):
        return "Cachorro: AuAu"

class Gato(Animal):
    def som(self):
        return "Gato: Miau"

def fazer_som(animal):
    print(animal.som())

if __name__ == "__main__":
    cachorro = Cachorro()
    gato = Gato()

    fazer_som(cachorro)
    fazer_som(gato) 