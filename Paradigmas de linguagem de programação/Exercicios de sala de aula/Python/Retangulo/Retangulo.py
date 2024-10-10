class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)

    def exibir_dados(self):
        print(f"O perímetro do retangulo é: {self.calcular_perimetro()}")
        print(f"A área do retangulo é: {self.calcular_area()}")

class main():
    ret = Retangulo(200, 300)
    ret.calcular_area()
    ret.calcular_perimetro()
    ret.exibir_dados()

if __name__ == "__main__":
    main()
