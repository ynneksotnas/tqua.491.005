# TODO
"""
Crie um programa que recebe o nome, a idade e a altura 
do usuário, e verifica se o usuário tem a idade e a altura 
mínima para entrar no brinquedo. Caso não tenha, o programa 
deverá barrar a entrada do usuário.
"""
#declaração de variáveis

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua idade: ").replace(",","."))

#saída de dados

if idade >= 14 and altura >= 1.60:
    print(f"{nome}, você pode entrar no brinquedo.")
else:
    print(f"{nome}, você não pode entrar no brinquedo.")