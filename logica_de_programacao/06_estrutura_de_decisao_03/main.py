"""
Programa que receba o nome e a média final de um
aluno, e o programa retorna se o aluno foi aprovado, se ficou
de recuperação, ou se foi reprovado, com sabe em sua média
final.
"""
# NOTE - a média deverá ser entre 0 e 10.
# NOTE - média para aprovação = 7. Recuperação = 5.

#declaração de variáveis
nome = input("Insira seu nome: ")
media = float(input("Informe a média do auno: ").replace(",","."))

#verifica se a média entra dentro do intervalo
if media >= 0 and media <=10:
    if media >= 7:
        print(f"{nome} está aprovado.")
    elif media >= 5:
        print(f"{nome} está de recuperação.")
    else:
        print(f"{nome} está reprovado.")
else:
    print("Valor da média inválida.")