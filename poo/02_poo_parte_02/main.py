#classe
class Pessoa:
    # atributos
    nome = "Kenny Martins"
    idade = 19
    email = "kenny@gmail.com"
    profissao = "programador"

    # metodos
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade}, trabalho como {self.profissao}, e meu e-mail é {self.email}.")

# algoritmo principal
if __name__ == "__main__":
    # instaciar a classe
    usuario = Pessoa()

    # executar o método
    usuario.apresentar()