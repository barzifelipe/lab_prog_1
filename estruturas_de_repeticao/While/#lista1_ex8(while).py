#lista1_ex8(while)

contador = 0
soma_idades = 0

while True:
    idade = int(input("Digite uma idade ou 0 para sair: "))
    if idade == 0:
        break
    if idade > 21:
        contador += 1
        soma_idades += idade
        
media_idades = soma_idades/contador
print(f"A média das idades é: {media_idades:.0f}")