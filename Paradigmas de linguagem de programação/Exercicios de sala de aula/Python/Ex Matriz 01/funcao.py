#Luan Victor Santana de Macêdo - P6D

import random

def gerarNumeros(numeros_existentes):
    numero = random.randint(0, 99)

    while numero in numeros_existentes:
        numeros = random.randint(0, 99)

    return numero

def gerarCartela():
    numeros = set()
    cartela = []

    for i in range(5):
        numero = gerarNumeros(numeros)
        numeros.add(numero)
        cartela.append(numero)

    return cartela

def exibirCartela(cartela):

    print("Cartela de bingo: ")
    for numero in cartela:
        print(numero)