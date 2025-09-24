# Ex4

somaNotas = 0
contador = 0

while True:
    nome = input("Digite seu nome (ou 0 para sair): ")
    if nome == "0":
         break

    nota = float(input("Digite sua nota: "))

    somaNotas += nota
    contador += 1

if contador > 0:
    mediaNotas = somaNotas / contador
    print(f"A média da turma foi: {mediaNotas:.2f}")
else:
    print("Nenhuma nota foi inserida.")
   