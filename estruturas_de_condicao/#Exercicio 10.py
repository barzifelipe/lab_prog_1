#Exercicio 10

salarioBruto = float(input("Digite seu salário bruto: "))

if salarioBruto < 1903.98:
    print("Você está isento!")
elif salarioBruto > 1903.99 and salarioBruto < 2826.65:
    valorDevido1 = (salarioBruto*0.07)-142.80
    print(valorDevido1)
elif salarioBruto > 2826.66 and salarioBruto < 3751.05:
    valorDevido2 = (salarioBruto*0.15)-354.80
    print(valorDevido2)
elif salarioBruto > 3751.06 and salarioBruto < 4664.68:
    valorDevido4 = (salarioBruto*0.225)-636.13
    print(valorDevido4)
else:
    valorDevido5 = (salarioBruto*0.275)-869.36
    print(valorDevido5)