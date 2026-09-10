biblioteca = []
class Livro:

    def __init__(self, titulo):
        biblioteca.append(self)
        self.codigo = len(biblioteca) #len é para ver o tamanho da lista
        self.titulo = titulo
        self.disponivel = True
        self.historico_emprestimos = []

    def emprestar(self, nome_usuario):
        if self.disponivel:
            self.disponivel = False
            self.historico_emprestimos.append(f'Emprestado para {nome_usuario}')
        else:
            print(f'Livro {self.titulo} indisponível')


    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            self.historico_emprestimos[-1] + " - DEVOLVIDO"
        #else:
            #print('Vo')

    def exibir_historico(self):
        for item in self.historico_emprestimos:
            print(item)

def listar_livros():
    for i in biblioteca:
                print(f'{i.codigo}. {i.titulo}')

 
livros = []

while True:
    opcao = input("Selecione uma opção:\n[0] Sair\n[1] Listar Livros\n[2] Cadastrar Livro\n[3] Selecionar Livro\n->")

    match(opcao):
        case "1":  
            listar_livros()
        case "2":
            Livro(input("Digite o nome do livro: \n->"))
        case "3":
            listar_livros()
            livro_escolhido = int(input("Digite o numero do livro selecionado;\n->"))
            if livro_escolhido <= len(biblioteca) and livro_escolhido > 0:
                while True:
                    opcao = input("Selecione uma opção: \n[1] Emprestar\n[2] Devolver\n[3] Ver Histórico\n[0] Voltar\n->")
                    match(opcao):   
                        case "1":
                            biblioteca[livro_escolhido-1].emprestar(input('Digite seu nome:\n->'))
                        case "2":
                            biblioteca[livro_escolhido-1].devolver()
                        case "3":
                            biblioteca[livro_escolhido-1].exibir_historico()
                        case "0":
                            break
                        case _:
                            print("Opção inválida, tente novamente.")
                    break
            else:
                print("Livro inexistente, tente de novo.")

        case "0":
            break
        
        case _:
            print("Opção inválida, tente novamente.")




   
        
    