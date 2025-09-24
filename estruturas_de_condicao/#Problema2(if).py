#Problema2(if)

horas = int(input("Quantas foram as horas trabalhadas no mês? "))
salarioBruto = horas*19.50

if salarioBruto > 2500:
 salarioLiquido = salarioBruto - (salarioBruto*0.25)
 print(f"Seu salário líquido é {salarioLiquido:.2f}")