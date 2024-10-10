class Animal:
    def som(self):
        raise NotImplementedError

class Vaca(Animal):
    def som(self):
        return "Vaca: Muuuu"

class Cabra(Animal):
    def som(self):
        return "Cabra: Bééééé"

def fazer_som_animais(animais):
    for animal in animais:
        print(animal.som())

if __name__ == "__main__":
    animais = [Vaca(), Cabra()]
    fazer_som_animais(animais)
