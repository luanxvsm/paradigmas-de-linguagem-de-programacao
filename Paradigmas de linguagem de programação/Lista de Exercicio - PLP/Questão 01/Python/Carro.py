class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

carro1 = Carro("Hyundai", "HB20x", 2015)
carro2 = Carro("Fiat", "Punto", 2012)
carro3 = Carro("Ford", "EcoSport", 2019)

carro1.detalhes()
carro2.detalhes()
carro3.detalhes()
