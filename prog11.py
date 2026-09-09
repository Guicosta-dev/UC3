class Filme: #class serve para criar uma classe, ou seja, um modelo para criar objetos.
             #Nesse caso, estamos dizendo:
             #Todo objeto do tipo Filme terá certas informações e comportamentos.
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.assistido = False

    def marcar_como_assistido(self):  #snakecase (Padrão fora da classe)
        self.assistido = True
        print(f"O {self.titulo} foi assistido {self.assistido}!")


filme1 = Filme("Interestelar", "165")
filme2 = Filme("Shrek","180")

filme1.marcar_como_assistido()
