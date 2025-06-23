chaves = ('Nome', 'Idade', 'E-mail', 'Profissão')
pessoas = [
    {
        chaves[0]: "Alex Machado",
        chaves[1]: 40,
        chaves[2]: "alexmachado@gmail.com",
        chaves[3]: "CEO"
    },
    {
        chaves[0]: "Maria da Silva",
        chaves[1]: 25,
        chaves[2]: "maria@gmail.com",
        chaves[3]: "Assistente Administrativo"
    }
]

# inserindo nome dicionario
pessoa = {}

# inserindo dados no novo dicionario
try:
    for chave in chaves:
        if chave == 'Idade':
            pessoa[chave] = int(input("Informe a Idade: "))
        else:
            pessoa[chave] = input(f"Informe {chave}: ")
    pessoas.append(pessoa)
    print(f"{pessoa.get(chave[0])} inserido com sucesso")
except Exception as e:
    print(f"Não foi possível cadastrar nova pessoa. {e}.")
finally:
    for pessoa in pessoas:
        for chave in pessoa:
            print(f"{chave}: {pessoa.get(chave)}.")
        print(f"\n{'-'*40}\n")