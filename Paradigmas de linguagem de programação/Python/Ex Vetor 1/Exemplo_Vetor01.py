# Luan Victor Santana de Macêdo - P6D

from soma import Vetor, Preenche, definirPosicoes, SomarPosicoes


def main():
    vetor1 = Vetor()
    Preenche(vetor1)
    x, y = definirPosicoes()
    soma = SomarPosicoes(x, y, vetor1)
    print("A soma dos vetores selecionados é: {}".format(soma))

if __name__ == "__main__":
    main()