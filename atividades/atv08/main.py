"""
# TODO - atividade - Crie um programa onde o usuário possa fazer as seguintes operações:
- Calcular área de umquadrado
- Calcular área de um retângulo
- Calcular área de um triângulo
- Calcular área de um trapézio
- Sair do programa
# NOTE - o usuário deverá escolher a operação em um menu
# NOTE - o programa deverá ser feito com funções
"""
# biblioteca
import os

# funções
def quadrado(l):
    a = 1**2
    return a
def retangulo(b,h):
    a = b*h
    return a
def triangulo(b,h):
    a = (b*h)/2
    return a
def trapezio(B,b,h):
    a = (B+b)*h/2
    return a

#algoritmo principal:
if __name__ == "__main__":
    while True:
        try:
            #menu
            print("1 - Calcular área de um quadrado")
            print("2 - Calcular área de um retângulo")
            print("3 - Calcular área de um triângulo")
            print("4 - Calcular área de um trapézio")
            print("5 - Sair do programa")
            opcao = input("Informe a opreção desejada: ").strip()
            os.system("cls" if os.name == "nt" else "clear")
            match opcao:
                case "1":
                    l = float(input("Informe o valor do lado do quadrado: ").replace(",","."))
                    area = quadrado(l)
                    print(f"A área do quadrado é {area}.")
                    continue
                case "2":
                    b = float(input("Informe o valor da base do retângulo: ").replace(",","."))
                    h = float(input("Informe o valor da altura do retângulo: ").replace(",","."))
                    area = retangulo(b,h)
                    print(f"A área de retângulo é {area}.")
                    continue
                case "3":
                    b = float(input("Informe o valor da base do triângulo: ").replace(",","."))
                    h = float(input("Informe o valor da altura do triângulo: ").replace(",","."))
                    area = triangulo(b,h)
                    print(f"A área de um triângulo é {area}.")
                    continue
                case "4":
                    b = float(input("Informe o valor da base menor do trapézio: ").replace(",","."))
                    B = float(input("Informe o valor da base maior do trapézio: ").replace(",","."))
                    h = float(input("Informe o valor da altura do trapézio: ").replace(",","."))
                    area = trapezio(B,b,h)
                    print(f"A área do trapézio é {area}.")
                    continue
                case "5":
                    print("Programa finalizado.")
                    break
                case _:
                    print("Opção inválida.")
                    continue
        except Exception as e:
            print(f"Não foi possível calcular: {e}.")
            continue

