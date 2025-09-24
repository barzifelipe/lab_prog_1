#lista1_ex1(while)

while True:
    nota = float(input("Qual é a sua nota? "))
    if 0 <= nota <= 10:
        print(f"Nota válida : {nota:.2f}")
        break
    else: 
       print("Valor inválido. Tente novamente. ")
