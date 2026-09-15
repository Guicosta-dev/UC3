class RelatorioPDF:
    def gerar(self,dados):
        return(f"Gerando arquivo PDF com os dados: {dados}")

class RelatorioExcel:
    def gerar(self,dados):
         return(f"Gerando planilha Excel com os dados: {dados}")


relatorios = [RelatorioPDF(),RelatorioExcel()]

for i in relatorios:
    print(i.gerar("...dados"))