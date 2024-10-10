class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self):
        self.empregados = []

    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

empresa = Empresa()
empresa.adicionar_empregado(Empregado("João", "Desenvolvedor", 3000.00))
empresa.adicionar_empregado(Empregado("Maria", "Gerente", 5000.00))

for empregado in empresa.empregados:
    print(f"{empregado.nome} - {empregado.cargo} - {empregado.salario}")
