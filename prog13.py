class ContaBancaria:

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Valor sacado: R$ {valor:.2f}")
        else:
            print("Saque negado: Saldo insuficiente.")


conta = ContaBancaria("Guilherme")

conta.depositar(100)

conta.sacar(150)

conta.sacar(50)

print(f"Saldo final: R$ {conta.saldo:.2f}")