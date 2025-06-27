import os

"""
Crie um programa que receba do usuário os seguintes dados:
- Nome
- CPF
- Data de Nascimento
- E-mail
- Gênero
- Telefone
- Endereço
- Altura em metros
- Peso em Kg
- Tipo Sanguíneo
Ao final, o programa  exibe esses dados
# NOTE - deve ser feito utilizando o conceito de dicionário
"""

pessoa = {}
print("\nInforme os seus dados:")
try:
    pessoa['nome'] = (input("Informe o nome:")).title().strip()
    pessoa['cpf'] = int(input("Informe o CPF:"))
    pessoa['dn'] = (input("Informe a Data de Nascimento:")).strip()
    pessoa['email'] = (input("Informe o E-mail:")).lower().strip()
    pessoa['genero'] = (input("Informe o Gênero:")).title().strip()
    pessoa['telefone'] = int(input("Informe o Telefone:"))
    pessoa['endereco'] = (input("Informe o Endereço:")).strip()
    pessoa['altura'] = float(input("Informe a Altura em m:"))
    pessoa['peso'] = float(input("Informe O peso em kg:"))
    pessoa['sangue'] = (input("Informe o Tipo Sanguíneo:")).title().strip()
    os.system("cls")
    for dc, valor in pessoa.items():
        print(f"{dc.capitalize()}: {valor}")
except Exception as e:
    print(f"Não foi possível inserir o valor. {e}.")