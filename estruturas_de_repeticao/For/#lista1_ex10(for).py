# lista1_ex10(for)
from fractions import Fraction

numero = int(input("Digite um numero: "))
soma = Fraction(0)

for i in range (1, numero + 1):
    print (i)
    soma += Fraction(1,i)
print(soma)