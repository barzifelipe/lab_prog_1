# lista2_ex2(for)

# Escreva um programa que recebe um número n e calcula a soma de todos os números de 1 até n

numero = int(input("Digite um número: "))
soma = 0
for i in range(0, numero + 1):
    soma += i
print(soma)