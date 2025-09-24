# Ex1

while True:
    nota = float(input("Digite uma nota: "))
    if 0 <= nota <= 10:
         print(f"Sua nota foi {nota}")
         break 
    else:
         print("Valor inválido. Por favor tente novamente")