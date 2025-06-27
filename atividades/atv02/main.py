"""
Crie um programa que receba o nome do usuário e informe o 
menu abaixo:
Sala 1 - A roda Quadrada - Livre
Sala 2 - A volta dos que não foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As trança do Rei Careca - 15 anos
Sala 5 - A vingaça do frango Assado - 18 anos
O usuário deverá escolher a sala do filme que deseja
assistir, e o programa deverá:
- Liberar a entrada do usuário e encerrar, caso o usuário
tenha a idade mínima, ou maior.
- Bloquear a entrada do usuário e pedir para o mesmo
escolher outro filme, caso não tenha a idade mínima.
"""

# TODO

nome = input("Informe seu nome: ").strip()
idade = int(input("Informe sua idade: ").strip())
print(f"{'-'*20} Calculadora {'-'*20}")
print("Sala 1 - A roda Quadrada - Livre")
print("Sala 2 - A volta dos que não foram - 12 anos")
print("Sala 3 - Poeira em Alto Mar - 14 anos")
print("Sala 4 - As trança do Rei Careca - 15 anos")
print("Sala 5 - A vingaça do frango Assado - 18 anos")
while True:
    verificar = input("Pressione o número da sala do filme que quer assistir.").strip()
    match verificar:
        case "1": 
            if idade >= 1:
                print("Sala 1, liberada.")
                break
            else:
                print("Você nem é gente.")
                break
        case "2":
            if idade >= 12:
                print("Sala 2, liberada.")
                break
            else:
                print("Menor de idade, escolha outra sala.")
                continue
        case "3": 
            if idade >= 13:
                print("Sala 3, liberada.")
                break
            else:
                print("Menor de idade, escolha outra sala.")
                continue
        case "4":
            if idade >= 15:
                print("Sala 4, liberada.")
                break
            else:
                print("Menor de idade, escolha outra sala.")
                continue
        case "5":
            if idade >= 18:
                print("Sala 5, liberada.")
                break
            else:
                print("Menor de idade, escolha outra sala.")
                continue
        case _:
            print("Sala não selecionada, selecione uma sala para poder assistir um.")
            continue