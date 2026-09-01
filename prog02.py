valor_total = 10.0
saldo_usuario = 9.0
pergunta = input("Voce tem cupom? s/n\n")
cupom_valido = False

if pergunta =="s":
    cupom_valido = True
    
else:
    cupom_valido = False

if cupom_valido:

    valor_total*= 0.9

print(valor_total)
    

if saldo_usuario >= valor_total:
    print("201 created - Pedido realizado com sucesso!")
else:
    print("402 Payment required - Saldo insuficiente")


print(valor_total)
