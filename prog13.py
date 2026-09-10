class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Você depositou R${valor}. Saldo atual: R${self.saldo}.')

    def sacar(self, valor):
        if valor>self.saldo:
            print('Saldo insuficiente :(')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}.')

conta = ContaBancaria('Guilherme')

conta.depositar(100)
conta.sacar(150)
conta.sacar(50)
