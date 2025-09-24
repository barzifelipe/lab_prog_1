# lista2_ex1(for)
# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Converte a palavra para minúsculas para padronizar as comparações
palavra = palavra.lower()

# Cria uma lista com as vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# Inicializa a contagem de vogais
contagem = 0


for i in palavra:
    if i in vogais:
        contagem += 1

# Exibe o resultado
print("A palavra", palavra, "possui", contagem, "vogais.")

