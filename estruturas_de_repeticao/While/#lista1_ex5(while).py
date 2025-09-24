#lista1_ex5(while)

maior_valor = None

while True:
    valor = float(input("Digite um valor ou 0 para sair: "))
    if valor == 0:
        break
    if maior_valor is None or valor > maior_valor:
       maior_valor = valor
    
    if maior_valor is not None:
        print(f"O maior valor digitado foi {maior_valor}")
    else:
        print("Nenhum valor válido foi digitado: ")