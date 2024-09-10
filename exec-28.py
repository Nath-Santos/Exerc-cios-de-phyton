#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
print("Escreva o 1º numero")
num1 =float(input())

print("Escreva o 2º numero")
num2 =float(input())

print("Escreva o 3º numero")
num3 =float(input())

if num1 > num2 and num1 > num3:
   print(num1)

elif num2 > num1 and num2 > num3:
   print(num2)

else:
  print(num3)
