"""
Crie um programa que receba o nome, o peso e a altura do usuário, 
e informe seu IMC (Índice de Massa Corporal) e informe seu diagnóstico
de acordo com o valor de seu IMC:
- Magro demais
- Peso normal
- Acima do peso
- Obeso
- Obesidade nível II
- Obesidade mórbida
"""

# TODO

print(f"{'-'*20} CALCULADORA IMC {'-'*20}")

nome = input("Informe seu nome: ").strip()
p = float(input("Informe seu peso: ").strip().replace(",","."))
a = float(input("Informe sua altura: ").strip().replace(",","."))

imc = p/a**2
print(f"IMC de {nome} é: {imc:,.2f}.")

if imc <= 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print("O seu IMC é Normal")
elif imc >= 25 and imc <= 29.9:
    print("Você está acima do peso.")
elif imc >= 30 and imc < 34.9:
    print("Você está obeso")
elif imc >= 35 and imc <= 39.9:
    print("O seu IMC é Obesidade nível II")
else:
    print("Obesidade mórbida.")