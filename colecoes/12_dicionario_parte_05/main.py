#lista de dicionarios
pessoas = [
    {
        'nome': "Fulano",
        'idade': 18,
        'email': "fulano@gmail.com",
        'profissão': "Programador"
    },
    {
        'nome': "Cicrano",
        'idade': 25,
        'email': "cicrano@gmail.com",
        'profissão': "DBA"
    },
    {
        'nome': "Beltrano",
        'idade': 30,
        'email': "beltrano@gmail.com",
        'profissão': "Gerente de Projetos"
    }
]

nova_pessoa = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'profissão': "CEO"
}
# adicionando novo dicionário a lista
pessoas.append(nova_pessoa)

#exibe nova lista de dicionários
print(f"\nNova Lista:\n")
for pessoa in pessoas:
    for chave in pessoa:
        print(f"{chave.capitalize()}: {pessoa.get(chave)}.")
    print(f"\n{'-'*40}\n")