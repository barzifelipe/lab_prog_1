# Ex2.1

import re  

while True:
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite uma senha: ")
   
    if len(senha) < 8:
        print("Erro. A senha deve ter pelo menos 8 caracteres.")
   
    elif not (re.search(r"[A-Za-z]", senha) and re.search(r"[0-9]", senha) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha)):
        print("Erro. A senha deve conter pelo menos uma letra, um número e um caractere especial.")
    
    else:
        print("Usuário e senha válidos!")
        break
