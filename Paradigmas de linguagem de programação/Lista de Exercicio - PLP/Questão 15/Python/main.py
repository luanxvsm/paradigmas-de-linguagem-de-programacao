class SaldoInsuficienteException(Exception):
    def init(self, message="Saldo insuficiente para realizar o saque"):
        self.message = message
        super().init(self.message)

class ContaBancaria:
    def init(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException()
        self.saldo -= valor
        return self.saldo

conta = ContaBancaria(100)
try:
    conta.sacar(150)
except SaldoInsuficienteException as e:
    print(e)