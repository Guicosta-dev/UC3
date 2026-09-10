armas_disponiveis = []
class Arma:

    def __init__(self, nome_arma, dano_extra):
        armas_disponiveis.append = (self)
        self.nome_arma = nome_arma
        self.dano_extra = dano_extra
        

class Personagem:

    def __init__(self, id_jogador,nome):
        self.id_jogador = id_jogador
        self.nome = nome
        self.vida = 100
        self.arma_equipada = None

    def equipar(self,objeto_arma):
        self.arma_equipada = objeto_arma

    def atacar(self, alvo):
        dano = 10

        if self.arma_equipada is not None:
            dano+= self.arma_equipada.dano_extra 
            
        alvo.vida = alvo.vida - dano

personagens = []
    