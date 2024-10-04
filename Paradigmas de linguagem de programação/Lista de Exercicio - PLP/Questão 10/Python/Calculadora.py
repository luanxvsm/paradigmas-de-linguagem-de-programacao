# Q10) Implemente uma classe Calculadora com métodos somar que aceita diferentes números
# de parâmetros (dois ou três números). Em Golang, use funções com nomes diferentes
# para diferentes quantidades de parâmetros

class Calculadora:

    def somar_dois(self, a, b):
        return a + b

    def somar_tres(self, a, b, c):
        return a + b + c

calc = Calculadora()

resultado1 = calc.somar_dois(5, 10)
print("Soma de 5 + 10 =", resultado1)

resultado2 = calc.somar_tres(5, 10, 15)
print("Soma de 5 + 10 + 15 =", resultado2)