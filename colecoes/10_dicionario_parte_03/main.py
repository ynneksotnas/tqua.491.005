#dicionario
usuario = {
    'nome': "Fulado de Tal",
    'idade': 18,
    'email': "fulano@gmail.com",
    'telefone': "(61) 98765-4321",
    'profissão': "Programador"
}
# usuario escolhe a chave que deseja aterar
chave = input("Informe o nome da chave que deseja alterar:").lower().strip()

#tratamento de exceção
try:
    if chave in usuario:
        usuario[chave] = input("Informe o novo valor: ").strip()
        print(f"Chave {chave} alterada com sucesso!")
    else:
        print("Não foi possível encontrar a chave requisitada.")
except Exception as e:
    print(f"Não foi possível alterar. {e}.")
finally:
    #exibe os novo valores no dicionário
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}.")