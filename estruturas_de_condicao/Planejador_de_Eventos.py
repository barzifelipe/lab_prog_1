print("Bem vindo ao Planejador de Eventos!")

quantidade_convidados = int(input("Quantos serão os convidados da sua festa? "))

if quantidade_convidados > 200:
    salgadinhos = int(input("Digite o número de salgadinhos planejado: "))
    
    if salgadinhos < 3500:
        print("Seus convidados sentirão fome. Providencie mais.")
    else:
        print("Salgadinhos suficientes.")

    docinhos = int(input("Digite o número de docinhos planejado: "))

    if docinhos < 1750:
        print("Seus convidados sentirão fome. Providencie mais.")
    else:
        print("Docinhos suficientes.")

if 100 < quantidade_convidados < 200:

    salgadinhos = int(input("Digite o número de salgadinhos planejado: "))
    
    if salgadinhos < 2500:
        print("Seus convidados sentirão fome. Providencie mais.")
    else:
        print("Salgadinhos suficientes.")

    docinhos = int(input("Digite o número de docinhos planejado: "))

    if docinhos < 1250:
        print("Seus convidados sentirão fome. Providencie mais.")
    else:
        print("Docinhos suficientes.")

if quantidade_convidados < 100:

    salgadinhos = int(input("Digite o número de salgadinhos planejado: "))
    
    if salgadinhos < 1500:
        print("Seus convidados sentirão fome. Providencie mais.")
    else:
        print("Salgadinhos suficientes.")

    docinhos = int(input("Digite o número de docinhos planejado: "))

    if docinhos < 750:
        print("Seus convidados sentirão fome. Providencie mais.")
    else:
        print("Docinhos suficientes.")







