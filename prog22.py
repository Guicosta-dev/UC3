class RelatorioPDF:
    def gerar(self,dados):
        print(f"Gerando arquivo PDF com os dados: {dados}")

class RelatorioExcel:
    def gerar(self,dados):
         print(f"Gerando planilha Excel com os dados: {dados}")

dados_pdf = RelatorioPDF()
dados_excel = RelatorioExcel()

lista = [dados_pdf,dados_excel]

for dado in lista:
    dado.gerar("Vendas de Maio")