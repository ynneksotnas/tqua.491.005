from classes import Pessoa

if __name__ == "__main__":
    usuario = Pessoa(
        nome="",
        idade=0,
        email="",
        telefone="",
        profissao="",
        peso=0.0,
        altura=0.0
        )

    usuario.nome = "Fulano"
    usuario.idade = "19"
    usuario.email = "fulano@gmail.com"
    usuario.telefone = "(11) 32938-1231"
    usuario.profissao = "programador"
    usuario.peso = 100
    usuario.altura = 1.95

    print(f"{usuario} tenho {len(usuario.idade)} anos. Segue meus dados:")
    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Profissão: {usuario.profissao}")
    print(f"Peso: {usuario.peso}")
    print(f"Altura: {usuario.altura}")
    
    del(usuario)