#lista1_ex7(if)

print ("Bem vindo ao Planejador de Eventos!")

quantidade_convidados = int(input("Quantos serão os convidados da sua festa? "))

if quantidade_convidados > 200:
   
   salgadinhos = int(input(f"Digite o número de salgadinhos palnejado: "))
   
   if salgadinhos < 3500:
      print ("Número de salgadinhos insuficiente")
   else:
     print ("Seus convidados não sentirão fome")
 
     docinhos = int(input(f"Digite o número de docinhos planejado: ") )

     if docinhos < 1750:
      print ("Número de salgadinhos insuficiente")
     else:
      print ("Seus convidados não sentirão fome")

if 100 < quantidade_convidados < 200:

   salgadinhos = int(input(f"Digite o número de salgadinhos palnejado: "))
   
   if salgadinhos < 2500:
      print ("Número de salgadinhos insuficiente")
   else:
     print ("Seus convidados não sentirão fome")

     docinhos = int(input(f"Digite o número de docinhos planejado: ") )

     if docinhos < 1250:
      print ("Número de salgadinhos insuficiente")
     else:
      print ("Seus convidados não sentirão fome")


if quantidade_convidados < 100:
   
    salgadinhos = int(input(f"Digite o número de salgadinhos palnejado: "))
   
    if salgadinhos < 1500:
      print ("Número de salgadinhos insuficiente")
    else:
     print ("Seus convidados não sentirão fome")

     docinhos = int(input(f"Digite o número de docinhos planejado: ") )

     if docinhos < 750:
      print ("Número de docinhos insuficiente")
     else:
      print ("Seus convidados não sentirão fome")



