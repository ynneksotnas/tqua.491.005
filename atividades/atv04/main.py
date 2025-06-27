import os

# TODO - atividade
"""
Crie um programa em que o usuário pode escolher entre:
- Inserir um nome em uma lista
- Exibir a lista de nomes
- Pesquisar por um nome na lista
- Alterar um nome da lista
- Excluir um nome da lista
- Sair do programa
"""

carrinho = [""]
while True:
    item = input("Informe o item: ").capitalize().strip()
    carrinho.append(item)
    print(f"{item} inserido com sucesso!")
    confirmar = input("Deseja adicionar mais um item? (s/n)").lower().strip()
    match confirmar:
        case "s":
            continue
        case "n":
            break
        case _:
            print("Opção inválida.")
            continue
while True:
    pesquisa = input("Para ter certeza, informe um item que colocou na lista. ").capitalize().strip()
    if pesquisa == item:
        print(f"{pesquisa} foi inserido.")
    else:
        print(f"Você não inseriu este item.")
        continue
    try:
        i = int(input("Informe o índice que seja alterar: "))
        if i >= 0 and i < len(item):
            item[i] = input("Informe o novo nome: ")
            print("Nome alterado com sucesso.")
        else:
                print("Índice inválido.")
    except Exception as e:
        print(f"Não foi possível alterar item da lista. {e}.")
        continue
while True:
    try:
        i = int(input("Informe o índice que deseja excluir: "))
        if i >= 0 and i < len(nomes):
            del(nomes[i])
            print("Nome excluído com sucesso.")
        else:
            print("Índice inválido.")
    finally:
        continue
while True:
    left = input("Deseja sair do programa? (s/n)")
    match left:
        case "s":
            break
        case "n":
            continue
for item in carrinho:
    print(item)

    # NÃO TERMINADO
