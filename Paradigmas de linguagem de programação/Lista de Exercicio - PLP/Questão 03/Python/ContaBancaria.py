class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial
        
    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depositados R${valor:.2f} na conta de {self.__titular}.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Sacados R${valor:.2f} da conta de {self.__titular}.")
        elif valor > self.__saldo:
            print("Saldo insuficiente para o saque.")
        else:
            print("Valor inválido para saque.")

conta = ContaBancaria("Luan", 1700.00)

print(f"Saldo inicial de {conta._ContaBancaria__titular}: R${conta.get_saldo():.2f}")

conta.depositar(500.00)
print(f"Saldo após depósito: R${conta.get_saldo():.2f}")

conta.sacar(300.00)
print(f"Saldo após saque: R${conta.get_saldo():.2f}")

conta.sacar(2000.00)
print(f"Saldo após tentativa de saque: R${conta.get_saldo():.2f}")
