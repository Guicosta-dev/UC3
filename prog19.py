
class Usuario:
  def __init__(self, login, senha):
    self.__login = login
    self.__senha = senha

  def alterar_senha(self, senha_antiga, nova_senha):
    if senha_antiga == self.__senha:
        self.__senha = nova_senha
        print("Senha alterada com sucesso!")

    else:
        print("Senha atual incorreta")

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

usuario = Usuario(login, senha)
print("\n Usuario cadastrado com sucesso!")

senha_antiga = input("Digite sua senha atual: ")
nova_senha = input("Digite sua nova senha: ")
usuario.alterar_senha(senha_antiga,nova_senha)
