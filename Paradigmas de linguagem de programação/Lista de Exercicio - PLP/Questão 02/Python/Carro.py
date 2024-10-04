# Q2) Adicione um método acelerar e frear à classe Carro que altere um atributo
# velocidade. Crie um método para exibir a velocidade atual

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 

    def detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"{self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} freou para {self.velocidade} km/h.")

    def exibir_velocidade(self):
        print(f"A velocidade atual do {self.modelo} é {self.velocidade} km/h.")

carro1 = Carro("Hyundai", "HB20x", 2015)
carro2 = Carro("Fiat", "Punto", 2012)
carro3 = Carro("Ford", "EcoSport", 2019)

carro1.detalhes()
carro2.detalhes()
carro3.detalhes()

carro1.acelerar(30)
carro1.exibir_velocidade()
carro1.frear(10)
carro1.exibir_velocidade()

carro2.acelerar(50)
carro2.exibir_velocidade()
carro2.frear(20)
carro2.exibir_velocidade()

carro3.acelerar(40)
carro3.exibir_velocidade()
carro3.frear(40)
carro3.exibir_velocidade()
