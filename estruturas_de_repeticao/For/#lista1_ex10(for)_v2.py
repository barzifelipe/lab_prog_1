# lista1_ex10(for)_v2

from fractions import Fraction

numero = int(input("Digite um número: "))

soma = Fraction(0)

print("Somando as frações:")
for i in range(1, numero + 1):
    fracao = Fraction(1, i)
    soma += fracao
    print(f"{soma - fracao} + {fracao} = {soma}")  

print("\nA soma total das frações de 1 até 1/", numero, "é:", soma)