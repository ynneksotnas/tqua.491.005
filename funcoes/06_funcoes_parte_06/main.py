import os
import equacoes as eq
while True:
    try:
        print("1 - Calcular equação do 1° grau.")
        print("2 - Calcular equação do 2° grau.")
        print("3 - Sair do programa.")
        opcao = input("Informe a operação desejada:").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                a = float(input("Informe o valor de a: ").replace(",","."))
                b = float(input("Informe o valor de b: ").replace(",","."))
                result = eq.equacao1(a, b)
                print(f"{a}x + {b} = 0")
                print(f"x = {result}")
            case "2":
                a = float(input("Informe o valor de a: ").replace(",","."))
                b = float(input("Informe o valor de b: ").replace(",","."))
                c = float(input("Informe o valor de c: ").replace(",","."))
                os.system("cls" if os.name == "nt" else "clear")
                result = eq.equacao2(a,b,c)
                for x in result:
                    print(x)
                continue
            case "3":
                print("Programa encerrado.")
                break
            case "_":
                print("Operação inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível calcular. {e}.")
        continue
