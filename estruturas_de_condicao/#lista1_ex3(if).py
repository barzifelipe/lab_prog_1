#lista1_ex3(if)

nota = float(input("Qual é a sua média? "))
aulas = int(input("Quantas aulas você teve nessa disciplina? "))
faltas = int(input("Quantas faltas você teve? "))


if nota < 6.0 or faltas >= 0.25*aulas:
    print("Você está reprovado!")
else:
    print("Você esta aprovado")

 