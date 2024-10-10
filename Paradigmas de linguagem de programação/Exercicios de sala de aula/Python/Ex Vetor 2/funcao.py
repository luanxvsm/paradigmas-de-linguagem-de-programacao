#Luan Victor Santana de Macêdo - P6D

def Vetor():
    vetor = []
    return vetor

def leitura(Vetor):
    # fazer a leitura e preenchimento dos elementos do vetor.
    for i in range(10):
        Vetor.append(int(input("Digite o elemento %d: " % i)))

def maiorValor(Vetor):
    maior = Vetor[0]
    for i in range(1, len(Vetor)):
        if Vetor[i] > maior:
            maior = Vetor[i]
    return maior

def menorValor(Vetor):
    menor = Vetor[0]
    for i in range(1, len(Vetor)):
        if Vetor[i] < menor:
            menor = Vetor[i]
    return menor

def imprimindo(maior, menor):
    print("O maior elemento do vetor é %d." % maior)
    print("O menor elemento do vetor é %d." % menor)