# Q12) Em Python,
# sobrecarregue o operador + para somar dois objetos Produto baseados no preço. Em Java
# e Golang, crie métodos que permitam essa funcionalidade.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __add__(self, other):
        return Produto(self.nome + " & " + other.nome, self.preco + other.preco)

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {self.preco}"

produto1 = Produto("Produto A", 50)
produto2 = Produto("Produto B", 30)

produto_soma = produto1 + produto2 
print(produto_soma)