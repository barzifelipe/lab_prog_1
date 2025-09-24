#lista1_ex6(while)

menor_valor = None

while True:
    valor = float(input("Digite um valor ou 0 para sair: "))
    if valor == 0:
        break
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor

    if menor_valor is not None:
        print(f"O menor valor é: {menor_valor}")
    else:
        print("Nenhum valor válido foi digitado.")