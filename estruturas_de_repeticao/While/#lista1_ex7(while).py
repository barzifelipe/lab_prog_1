#lista1_ex7(while)

contador = 0

while True:
    idade = int(input("Digite uma idade ou 0 para sair: "))
    if idade == 0:
        break
    if idade >= 18:
        contador += 1

print(f"O número de idades iguais ou superiores a 18 foi: {contador}")