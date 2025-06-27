"""
Crie um programa que receba do usuário dois números 
reais, e uma das 4 operações da matemática informadas
pelo usuário, e faça o cálculo correspondente.
"""

# NOTE - O programa so se encerrará caso o usuário informe isso no programa.
# TODO

while True:
    x = int(input("Informe o número X: ").strip())
    y = int(input("Informe o número Y: ").strip())

    print(f"{'-'*20} Calculadora {'-'*20}")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    calculo = input("Informe a operação: ").strip()

    match calculo:
        case "1":
            print(f"A soma é igual a {x+y}")
        case "2":
            print(f"A subtração é igual a {x-y}")
        case "3":
            print(f"A multiplicação é igual a {x*y}")
        case "4":
            print(f"A divisão é igual a {x/y}")
        case _:
            print("Opção inválida.")
            continue

    continua = input("Quer continuar? s/n").lower().strip()
    match continua:
        case "s":
            continue
        case "n":
            break