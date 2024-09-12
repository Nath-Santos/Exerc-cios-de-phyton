#dado o algoritmo, faça um teste de mesa  que complete o quadro  a seguir:
print("Escreva o valor do lado X")
valorX  = float(input())

print("Escreva o valor do lado Y")
valorY = float(input())



valorZ = (valorX * valorY) + 5

if   valorZ <= 0:
   print("A" +str(valorZ))
   
elif valorZ <= 100:
   print("B" +str(valorZ))
   
else:
    print("C")
