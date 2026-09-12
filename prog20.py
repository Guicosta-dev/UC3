class ProcessadorDePagamento:
    def _conectar_banco(self):
        print("Conectando com banco de dados...")

    def _autenticar_token(self):
        print("Autenticando transação...")

    def _deduzir_saldo(self, valor):
        self.valor = valor
        print(f"Deduzindo R${valor} do saldo")

    def processar_compra(self, valor):
        self._conectar_banco()
        self._autenticar_token()
        self._deduzir_saldo(valor)

processador = ProcessadorDePagamento()

processador.processar_compra(100)

print("Compra finalizada com sucesso!")
