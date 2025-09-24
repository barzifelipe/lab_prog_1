# Ex2

while True:
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite uma senha: ")
    if usuario == senha:
        print("Erro. Sua senha é igual ao nome de usuário.")
    else:
        print("Usuário e senha válidos! ")
        break
        