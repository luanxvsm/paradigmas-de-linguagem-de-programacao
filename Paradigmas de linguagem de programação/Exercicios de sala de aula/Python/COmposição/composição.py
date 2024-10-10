class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = nome

    def adicionar_endereco(self, endereco):
        self.endereco = endereco

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        if self.endereco:
            print("Endereço: ")
            self.endereco.mostrar_endereco()
        else:
            print("Endereço não disponivel")

class Endereco:
    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def mostrar_endereco(self):
        print(f"Rua: {self.rua}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}")

class Empresa:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Funcionarios da empresa {self.nome}: ")
        for funcionario in self.funcionarios:
            print(funcionario.nome)

endereco1 = Endereco("Av. Principal", "Cidade A", "Estado X", "12345-678")
pessoa1 = Pessoa("João", 30)
pessoa1.adicionar_endereco(endereco1)

endereco2 = Endereco("Av. Epitacio", "Cidade B", "Estado Y", "12345-978")
pessoa2 = Pessoa("Maria", 18)
pessoa2.adicionar_endereco(endereco2)

empresa = Empresa("Empresa AeC", "123456789123")
empresa.contratar_funcionario(pessoa1)
empresa.contratar_funcionario(pessoa2)

empresa.listar_funcionarios()








