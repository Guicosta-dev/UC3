itens_estoque = [12, 3, 8, 2, 15, 4, 20]

estoque_critico = 0
print("Estoque crítico")
for i in itens_estoque:
    if i < 5:
        estoque_critico+=1

print(f"Existem {estoque_critico} itens com estoque crítico")