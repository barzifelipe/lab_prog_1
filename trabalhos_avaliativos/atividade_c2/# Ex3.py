#Ex3

maiorAltura = None
menorAltura = None
maiorPeso = None
menorPeso = None
codigoMaiorAltura = 0
codigoMenorAltura = 0
codigoMaiorPeso = 0
codigoMenorPeso = 0

somaAltura = 0
somaPeso = 0
contador = 0

while True:
    codigo = int(input("Digite seu código de matrícula (digite 0 para sair): "))
    if codigo == 0:
        break

    altura = float(input("Digite sua altura (em metros): "))
    peso = float(input("Digite seu peso (em kg): "))

   
    somaAltura += altura
    somaPeso += peso
    contador += 1

    
    if maiorAltura is None or altura > maiorAltura:
        maiorAltura = altura
        codigoMaiorAltura = codigo

    if menorAltura is None or altura < menorAltura:
        menorAltura = altura
        codigoMenorAltura = codigo

    
    if maiorPeso is None or peso > maiorPeso:
        maiorPeso = peso
        codigoMaiorPeso = codigo

    if menorPeso is None or peso < menorPeso:
        menorPeso = peso
        codigoMenorPeso = codigo


if contador > 0:
    mediaAltura = somaAltura / contador
    mediaPeso = somaPeso / contador

    print("\nResultados:")
    print(f"Cliente mais alto: Código {codigoMaiorAltura} com altura de {maiorAltura:.2f} m")
    print(f"Cliente mais baixo: Código {codigoMenorAltura} com altura de {menorAltura:.2f} m")
    print(f"Cliente mais pesado: Código {codigoMaiorPeso} com peso de {maiorPeso:.2f} kg")
    print(f"Cliente menos pesado: Código {codigoMenorPeso} com peso de {menorPeso:.2f} kg")
    print(f"Média das alturas: {mediaAltura:.2f} m")
    print(f"Média dos pesos: {mediaPeso:.2f} kg")
else:
    print("Nenhum cliente foi registrado.")
