# lista1_ex5(for)

soma_notas = 0
num_notas = 0

for contador in range(5):
    nota = float(input("Digite uma nota: "))
    soma_notas += nota 
    num_notas += 1

media = soma_notas/num_notas
print(soma_notas)
print(media)