# lista2_ex3(for)

#Peça ao usuário para inserir um número, e depois imprima a tabuada de multiplicação desse número de 1 até 10.

numero = int(input("Digite um número: "))

for multiplicador in range (1,11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")