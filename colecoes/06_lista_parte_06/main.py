# importe biblioteca
import os

# lista
nomes = [
    "Maria",
    "Ana",
    "Júlia",
    "Clara",
    "Laura",
    "Sofia",
    "Helena",
    "Isabela",
    "Luísa",
    "Beatriz",
    "Joana",
]

# deletando um item específico
del(nomes[4])

# exibe a nova lista
for nome in nomes:
    print(nome)

# exibe a lista original
for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}")

# usuário informe a posição da lista que deseja excluir
try:
    i = int(input("Informe o índice que desejar excluir: "))
except Exception as e:
    print(f"Não foi possível excluir")