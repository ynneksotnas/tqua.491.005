"""
# TODO - atividade: Crie um programa que receba os dados de dois objetos diferentes da mesma classe Pessoa. Os dados serão os seguintes:
- Nome
- Idade
- E-mail
- Telefone
- Gênero
- Tipo sanguíneo
- Já teve doença transmitida por sangue?
Suponha que o objeto 'usuario_2' esteja precisando de doação de sangue do 'usuario_1'. O programa deve informar os dados dos dois, e ao final, informar se o usuario_1 pode doar sangue para o usuario_2 ou não.
# NOTE - as duas últimas perguntas deverá ter uma resposta randômica.
"""

import random

class Pessoa:
    def __init__(self,nome,idade,email,telefone,genero,sangue,doenca,humor):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.genero = genero
        self.sangue = sangue
        self.doenca = doenca
        self.humor = humor

    def boas_vindas(self):
        return "Boa tarde!"
    def cumprimentar(self):
        return "Me chamo {self.nome} e tenho {self.idade} anos."
    def receber_doacao(self):
        return "Preciso de uma doação de sangue."
    def doar1(self):
        return "Que pena, já tive uma doença transmitida por sangue."
    def doar2(self):
        return "Nunca tive uma doença transmitida por sangue, bora lá!"
    def ofender(self):
        return "Sai pra lá o aidético."
    
if __name__ == "__main__":
    usuario_1 = Pessoa("", 0, "", "", "", "", "", "",bool(random.getrandbits(0,1)))
    usuario_2 = Pessoa("", 0, "", "", "", "", "", "",bool(random.getrandbits(0,1)))
    try:
        usuario_1.nome = input("Informe seu nome: ").title().strip()
        usuario_1.idade = int(input("Informe seu idade: ").strip())
        usuario_1.email = input("Informe seu e-mail:").lower().strip()
        usuario_1.telefone = input("Informe seu telefone: ")
        usuario_1.genero = input("Informe seu gênero: ").title().strip()
        usuario_1.sangue = input("Informe seu tipo sanguíneo: ").strip()
        usuario_1.doenca = input("Ja teve doença transmitida por sangue? (s/n)").lower().strip()

        usuario_2.nome = input("Informe seu nome: ").title().strip()
        usuario_2.idade = int(input("Informe seu idade: ").strip())
        usuario_2.email = input("Informe seu e-mail:").lower().strip()
        usuario_2.telefone = input("Informe seu telefone: ")
        usuario_2.genero = input("Informe seu gênero: ").title().strip()
        usuario_2.sangue = input("Informe seu tipo sanguíneo: ").strip()

        match usuario_1.doenca:
            case "s":
                print(f"Pessoa 1 - {usuario_1.boas_vindas()}")
                print(f"Pessoa 2 - {usuario_2.boas_vindas()}")
                
            case "n":
                ...
    except Exception as e:
        print("Não foi possível informar o valor.")