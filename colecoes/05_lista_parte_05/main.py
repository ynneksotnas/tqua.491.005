import os
# lista
frutas = [
    "Morango",
    "Banana",
    "Maçã",
    "Pêra",
    "Uva",
    "Maracujá",
    "Abacaxi",
    "Laranja",
    "Pêssego"
]

# mudando o valor dapêra para mamão
frutas[3] = "Mamão"

# exibe a lista
for fruta in frutas:
    print(fruta)

# usuário informa o índice da fruta que deseja alterar
try:
    i = int(input("Informe o número do índice a ser alterado: "))
    os.system("cls")
    if i >= 0 and i < len(frutas):
        print(f"Valor encontrado: {frutas[i]}.")
        frutas [i] = input("Informe o nome da nova fruta:")
        os.system("cls")
        print("Fruta alterada com sucesso.")
    else:
        print("Valor do índice inválido.")
except Exception as e:
    print(f"Não foi possível executar a operação. {e}")
finally:
    print("\nNova lista\n")
    for i in range(len(frutas)):
        print(f"Índice {i}: {frutas[i]}.")