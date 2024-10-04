#Luan Victor Santana de Macêdo - P6D

def Vetor():
    vetor = []
    return vetor

def Preenche(vetor):
    for i in range(10):
        vetor.append(int(input("Digite o valor do vetor {}: ".format(i))))
    return vetor

def definirPosicoes():
    x = int(input("Digite o valor da posição X do vetor: "))
    y = int(input("Digite o valor da posição Y do vetor: "))
    return x,y

def SomarPosicoes(x,y,vetor):
    return vetor[x] + vetor[y]