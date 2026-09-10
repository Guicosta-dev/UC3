class CarteiraDigital:

    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo_inicial = saldo_inicial

    def transferir_pix(self, valor, carteira_destino):
        if self.saldo_inicial >= valor:
            self.saldo_inicial -= valor
            carteira_destino.saldo_inicial += valor
            print(f"Transferência de R$ {valor} para {carteira_destino.nome_titular} realizada com sucesso!")
        else:
            print("Erro: Saldo insuficiente para realizar o PIX.")


cliente_a = CarteiraDigital("Jorge", 500.00)
cliente_b = CarteiraDigital("Pedro", 100.00)

cliente_a.transferir_pix(150.00, cliente_b)

print(f"Saldo do {cliente_a.nome_titular}: R$ {cliente_a.saldo_inicial}")
print(f"Saldo do {cliente_b.nome_titular}: R$ {cliente_b.saldo_inicial}")