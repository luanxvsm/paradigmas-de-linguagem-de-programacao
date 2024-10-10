from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Relatorio(Imprimivel):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def imprimir(self):
        print(f"Imprimindo relatório: {self.conteudo}")

class Contrato(Imprimivel):
    def __init__(self, detalhes):
        self.detalhes = detalhes

    def imprimir(self):
        print(f"Imprimindo contrato: {self.detalhes}")

relatorio = Relatorio("Relatório financeiro")
contrato = Contrato("Contrato de prestação de serviços")

relatorio.imprimir()
contrato.imprimir()
