# importações
import classes
import os

if __name__ == "__main__":
    # instancia objeto
    usuario = classes.PessoaFisica("","","","","","")
    empresa = classes.PessoaJuridica("","","","","","")

    while True:
        print("1 - Inserir dados do usuário.")
        print("2 - Inserir dados da empresa.")
        print("3 - Mostrar dados.")
        print("4 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                try:
                    usuario.nome = input("Informe o nome do usuário: ").title().strip()
                    usuario.cpf = input("Informe o CPF: ").strip()
                    usuario.profissao = input("Informe a profissão: ").title().strip()
                    usuario.email = input("Informe o e-mail: ").lower().strip()
                    usuario.endereco = input("Informe o endereço: ").title().strip()
                    usuario.telefone = input("Informe o telefone: ").strip()

                    os.system("cls" if os.name == "nt" else "clear")
                    
                    print(f"Dados de {usuario.nome} inseridos com sucesso!")
                except Exception as e:
                    print(f"Não foi possível inserir dados dos usuário. {e}.")
                finally:
                    continue
            case "2":
                try:
                    empresa.razao_social = input("Informe a razão social da empresa: ").strip().title()
                    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
                    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
                    empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
                    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()
                    empresa.telefone = input("Informe o telefone da empresa: ").strip()

                    os.system("cls" if os.name == "nt" else "clear")

                    print(f"Dados da empresa {empresa.nome_fantasia} inseridos com sucesso!")
                except Exception as e:
                    print(f"Não foi possível inserir dados da empresa. {e}.")
                finally:
                    continue

            case "3":    
                try:
                    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}\n")
                    usuario.exibir_dados()
                    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}\n")
                    usuario.exibir_dados()
                except Exception as e:
                    print(f"Não foi possível exibir os dados. {e}.")
            case "4":
                print("Programa encerrado.")
                break
            case "_":
                print("Opção Inválida.")
                continue