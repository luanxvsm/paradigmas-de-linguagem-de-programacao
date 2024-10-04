# Q11) Crie uma classe abstrata Funcionario com um método abstrato
# calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
# implementam calcularSalario de formas distintas

from abc import ABC, abstractmethod

class Funcionario(ABC):

    @abstractmethod
    def calcularSalario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, horas_trabalhadas, valor_por_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcularSalario(self):
        return self.horas_trabalhadas * self.valor_por_hora

class FuncionarioAssalariado(Funcionario):
    def __init__(self, salario_fixo):
        self.salario_fixo = salario_fixo

    def calcularSalario(self):
        return self.salario_fixo

horista = FuncionarioHorista(160, 25)
assalariado = FuncionarioAssalariado(3000)

print("Salário do funcionário horista:", horista.calcularSalario())
print("Salário do funcionário assalariado:", assalariado.calcularSalario())