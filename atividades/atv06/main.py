import os
"""
# TODO - Atividade: Crie um programa com um dicionário chamado 'usuario',
com o seguinte menu:
- Cadastrar nova chave
- Exibir vdados do usuário
- Alterar valor da chave
- Excluir chave
- Sair do programa
# NOTE - Os dados a serem inseridos precisam ter a ver com dados de usuário
"""
usuario = {}
while True:
    print(f"{'-'*20} MENU {'-'*20}")
    print("1 - Para inserir nova chave")
    print("2 - Para exibir dados usuário")
    print("3 - Para alterar valor da chave")
    print("4 - Para excluir chave")
    print("5 - Para sair do programa")
    opcao = input("Qual número deseja inserir? ")

    os.system("cls")
    match opcao:
        case "1":
                chave = input("Informe a chave que quer criar. ").strip().lower()
                usuario[chave] = input((f"Informe o valor do(a) {chave}: "))
                os.system("cls")
                print("Chave cadastrada com sucesso!")
                continue
        case "2":
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
                continue
        case "3":
            chave = input("Informe o nome da chave que deseja alterar: ").lower().strip()
            if chave in usuario:
                usuario[chave] = input("Informe o novo valor: ")
                os.system("cls")
                print(f"Valor {chave} alterado com sucesso!")
            else:
                os.system("cls")
                print("Não foi possível encontrar a chave")
                continue
        case "4":
            chave = input("Informe a chave que quer deletar. ").lower().strip()
            confirmacao = input(f"Tem certeza de que deseja excluir {chave}? (s/n)").lower().strip()
            os.system("cls")
            if confirmacao is "s":
                del usuario[chave]
                print("Chave excluída com sucesso!")
            else:
                print("Não foi possível achar a chave.")
            continuechave = input("Informe a chave que quer deletar. ").lower().strip()
            confirmacao = input(f"Tem certeza de que deseja excluir {chave}? (s/n)").lower().strip()
            os.system("cls")
            if confirmacao is "s":
                del usuario[chave]
                print("Chave excluída com sucesso!")
            else:
                print("Não foi possível achar a chave.")
            continue
        case "5":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue