class Cachorro: #TUDO QUE COMEÇA COM LETRA MAIUSCULA É UMA CLASSE!!!
    #Método Constructor
    def __init__(self, nome, raca, tamanho, cor_pelo): #ATRIBUTOS DA CLASSE 
        self.nome = nome  #SELF É O PROPIO OBJETO SENDO CONSTRUINDO
        self.raca = raca
        self.tamanho = tamanho
        self.cor_pelo = cor_pelo
        self.patas = 4

zeca = Cachorro("Zeca","Viralata","Médio","Caramelo")
brutus = Cachorro("Brutus","Pitbull", "Grande", "Preto")
mel = Cachorro("Mel","Yorkshire", "Pequeno", "Marrom")

zeca.patas = 3 #EXCESSAO!!!

print(zeca.nome)



class Usuario:
    def __init__(self, nome, email): #Se o atributo começa indefinido é para coloca-lo como parametro!!!
        self.nome = nome
        self.email = email
        self.ativo = True #AQUI O ATRIBUTO JA ESTA DEFINIDO
    
    #Método de uma classe
    def desativar_conta(self):
        self.ativo = False

    def mudar_nome(self):
        self.nome = input("Digite seu novo nome de usuário: ")
        
        
nova_conta = Usuario("Gustavo", "gustavo@gmail.com")

nova_conta.desativar_conta()

print(nova_conta.ativo)