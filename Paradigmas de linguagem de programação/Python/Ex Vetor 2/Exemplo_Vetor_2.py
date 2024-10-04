# Faça um programa em Python que receba do usuario 
# um vetor com 10 posições. Em seguida devera ser 
# impresso o maior e o menor elemento do vetor.
#Luan Victor Santana de Macêdo - P6D

from funcao import Vetor
from funcao import leitura
from funcao import maiorValor
from funcao import menorValor
from funcao import imprimindo

def main():
    vetor1 = Vetor()
    leitura(vetor1)
    maior = maiorValor(vetor1)
    menor = menorValor(vetor1)
    imprimindo(maior,  menor)

if __name__ == "__main__":
    main()
