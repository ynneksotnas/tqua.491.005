import os
"""
# TODO - Atividade: Crie um programa que faça as seguintes operações:
- Inserir dados de novo usuário
- Exibir lista e usuários
- Alterar dados de um usuário ja cadastrado
- Excluir usuário da lista
- Sair do programa
Os dados a serem cadastrados serão os seguintes:
- Nome
- Data de Nascimento
- E-mail
- CPF
- Telefone
- Profissão
- Gênero
# NOTE - a lista deve começar vazia
"""
chaves = ('Nome','Data de Nascimento','E-mail','CPF','Telefone','Profissão','Gênero')
lista = []
while True:
    usuario = {}
    print(f"{'-'*20} MENU {'-'*20}")
    print("1 - Cadastrar novo usuário")
    print("2 - Exibir lista e usuários")
    print("3 - Alterar dados de um usuário ja cadastrado")
    print("4 - Excluir usuário da lista")
    print("5 - Sair do programa")
    opcao = input("Seleciona qual deseja inserir: ")
    os.system("cls")
    match opcao:
        case "1":      
            try:
                for chave in chaves:
                    usuario[chave] = input(f"Informe {chave}: ").lower().strip()
                    os.system("cls")
                lista.append(usuario)
                print(f"{usuario.get(chave[0])} inserido com sucesso")
            except Exception as e:
                print(f"Não foi possível cadastrar novo usuário. {e}.")
        case "2":
            for usuario in lista:
                for chave in usuario:
                    print(f"{chave}: {usuario.get(chave)}.")
        case "3":
            chave = input("Informe o nome da chave que deseja alterar: ").strip()
            if chave in usuario:
                usuario[chave] = input("Informe o novo valor: ")
                os.system("cls")
                print(f"Valor {chave} alterado com sucesso!")
            else:
                os.system("cls")
                print("Não foi possível encontrar a chave")
                continue
        case "4":
            chave = input("Informe a chave que quer deletar. ").strip()
            confirmacao = input(f"Tem certeza de que deseja excluir {chave}? (s/n)").lower().strip()
            os.system("cls")
            if confirmacao == "s":
                del usuario[chave]
                print("Chave excluída com sucesso!")
            else:
                print("Não foi possível achar a chave.")
            continue
        case "5":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida")
            continue