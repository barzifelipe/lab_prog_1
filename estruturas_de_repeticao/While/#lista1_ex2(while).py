#lista1_ex2(while)

peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

while peso < 400 and altura < 3.00:

 imc =  peso/(altura*altura)

 if imc > 30:
    print("Você está obeso!")
    
 elif 25 < imc < 30:
    
    print("Você está acima do peso")
 elif 18.5 < imc < 25:
    
    print("Você está com o peso normal")
 elif imc < 18.5:
    print("Você está abaixo do peso")
 break