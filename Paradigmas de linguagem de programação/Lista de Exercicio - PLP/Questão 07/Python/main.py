class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []

    def adicionar_escola(self, escola):
        self.escolas.append(escola)

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)
        professor.adicionar_escola(self)

escola1 = Escola("Escola A")
escola2 = Escola("Escola B")

professor1 = Professor("Professor X")
professor2 = Professor("Professor Y")

escola1.adicionar_professor(professor1)
escola2.adicionar_professor(professor1)
escola1.adicionar_professor(professor2)

print(f"{professor1.nome} leciona em: {professor1.escolas[0].nome} e {professor1.escolas[1].nome}")
print(f"{escola1.nome} tem os professores: {escola1.professores[0].nome} e {escola1.professores[1].nome}")
