class Usuario:
    def __init__(self, login, senha):  
        self.login = login
        self.__senha = senha
         
    #Método GETTER - NÃO FAZ PARTE DO EXERCICIO
    def get_login(self):
      return self.__login    

    #Método SETTER
    def alterar_senha(self, senha_antiga):
        if senha_antiga == self.__senha:
            #só pergunta senha nova se acertar a antiga
            self.__senha = input("Digite a nova senha:\n->")
            print("Senha alterada com sucesso.")
        else:
            print("Acesso negado: Senha atual incorreta")


user = Usuario("admin", "123")

user.alterar_senha(input("Digite sua senha atual:\n->"))