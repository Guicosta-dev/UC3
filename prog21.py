class AssinaturaBase:
    plano = "Base"
    def __init__(self,usuario):
        self.usuario = usuario
              
    def calcular_preco(self):
        return 0.00

class AssinaturaPremium(AssinaturaBase):
    plano = "Premium"
    def __init__(self,usuario):
        super().__init__(usuario)

    def calcular_preco(self):
        return 49.90
        
class AssinaturaEstudante(AssinaturaBase):
    plano = "Estudante"
    def __init__(self,usuario):
        super().__init__(usuario)

    def calcular_preco(self):
        return 24.90

usuario_base = AssinaturaBase("Marcelo")
usuario_premium = AssinaturaPremium("Guilherme") 
usuario_estudante = AssinaturaEstudante("Duda")

print(f"\nPlano:{usuario_base.plano}") 
print(f"Usuário: {usuario_base.usuario}") 
print(f"Preço: R$ {usuario_base.calcular_preco():.2f}")

print(f"\nPlano:{usuario_premium.plano} ") 
print(f"Usuário: {usuario_premium.usuario}")
print(f"Preço: R$ {usuario_premium.calcular_preco():.2f}")

print(f"\nPlano:{usuario_estudante.plano}") 
print(f"Usuário: {usuario_estudante.usuario}") 
print(f"Preço: R$ {usuario_estudante.calcular_preco():.2f}")





   