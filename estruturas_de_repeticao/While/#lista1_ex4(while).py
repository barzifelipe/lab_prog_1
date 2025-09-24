#lista1_ex4(while)

contador = 0
soma = 0

while True:
    valor = float(input("Digite um valor ou digite 0 para sair: "))
    if valor == 0:
        break
    soma += valor
    contador += 1

if contador > 0:
    media = soma/contador
    print(f"O número de valores digitados foi: {contador}")
    print(f"A média dos valores é: {media}")
else:
    print("Nenhum valor válido foi inserido. ")