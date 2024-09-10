#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores
#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
print("Escreva o 1º numero")
num1 =float(input())

print("Escreva o 2º numero")
num2 =float(input())

print("Escreva o 3º numero")
num3 =float(input())

if num1 > num2 and num1 > num3:
   soma = num2 + num3

elif num2 > num1 and num2 > num3:
   soma = num1 + num3

else:
  soma = num1 + num2
  
  print("A soma dos maiores valores é igual a:" + str(soma))
