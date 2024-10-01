#7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

A = int(input ("digite quantos dias voce tem de vida: "))
B = int(input ("digite quantos meses voce tem de vida: "))
C= int(input ("digite quantos anos voce tem de vida: "))
if 12>=B:
   print ((365*C) + (30*B) + A, "dias vividos")
else:
      print("valor acima do limite de meses em uma ano")
