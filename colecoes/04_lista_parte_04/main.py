# lista de cidades
cidades = [
    "Brasília",
    "Rio de Janeiro",
    "São Paulo",
    "Goiânia",
    "Palmas",
    "São Luís",
    "Belém",
    "Fortaleza",
    "Salvador",
    "Porto Alegre",
    "Florianópolis",
    "Belo Horizonte",
    "Maceió",
    "Brasília",
    "Florianópolis",
    "Maceió",
    "Goiânia",
    "Brasília"
]

# usuário faz a pesquisa
pesquisa = input("Informe o nome da cidade a ser pesquisada: ").title().strip()

# procurar a lista
if pesquisa in cidades: #se o valor de pesquisas estiver dentro de cidades
    print(f"{pesquisa} encontrado!")
else:
    print(f"{pesquisa} não encontrado.")

#pesquisar quantas vezes tem um termo
quantidade = cidades.count(pesquisa)
print(f"{pesquisa} foi encontrado {quantidade} vezes na lista!")