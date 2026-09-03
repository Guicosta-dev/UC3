base_usuarios = [
{"id": 101, "nome": "Alice"},
{"id": 102, "nome": "Bruno"},
{"id": 103, "nome": "Carla"}
]


def encontrar_id(id):
    encontrado = False
    for i in base_usuarios:
        if id == i['id']:
            encontrado = True
            return(f"Usuário encontrado: {i["nome"]}")
     
    if not encontrado:
        return("Usuário não encontrado")

print(encontrar_id(int(input("Digite o ID do usuário que deseja encontrar: "))))        


#Funçao sem RETURN é so uma ação SEM ARMAZENAMENTO

#Função COM RETURN a ação dela é ARMAZENADA