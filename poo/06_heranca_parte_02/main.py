import classes
import os

if __name__ == "__main__":
    filho = classes.Filho("","","","",0.0,0.0)
    
    try:
        filho.nome = input("Informe o nome: ").strip().title()
        filho.email = input("Informe o e-mail: ").strip().lower()
        filho.telefone = input("Informe o telefone: ").strip()
        filho.genero = input("Informe o gênero: ").strip().title()
        filho.peso = float(input("Informe o peso: ").replace(",","."))
        filho.altura = float(input("Informe a altura: ").replace(",","."))

        os.system("cls" if os.name == "nt" else "cls")

        filho.exibir_info()
    except Exception as e:
        print(f"Não foi possível executar. {e}.")

