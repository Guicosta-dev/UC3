class CarteiraDigital:

    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial

    def transferir_pix(self, valor, carteira_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            carteira_destino.saldo += valor
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso!")
        else:
            print("Erro: Saldo insuficiente para realizar o PIX.")


cliente_a = CarteiraDigital("Cliente A", 500.00)
cliente_b = CarteiraDigital("Cliente B", 100.00)

cliente_a.transferir_pix(150.00, cliente_b)

print(f"Saldo do Cliente A: R$ {cliente_a.saldo:.2f}")
print(f"Saldo do Cliente B: R$ {cliente_b.saldo:.2f}")