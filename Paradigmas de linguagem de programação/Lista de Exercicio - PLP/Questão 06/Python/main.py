class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, motor):
        self.motor = motor

motor = Motor(310)
carro = Carro(motor)
print("Potência do motor:", carro.motor.potencia)
