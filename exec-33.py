#33) Ler dois valores e imprimir uma das três mensagens a seguir:

#‘Números iguais’, caso os números sejam iguais
#‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
#‘Segundo maior’, caso o segundo seja maior que o primeiro.

print("Escreva o 1º numero")
num1 =float(input())

print("Escreva o 2º numero")
num2 =float(input())

print("Escreva o 3º numero")
num3 =float(input())

if num1 == num2 and num1 == num3:
   print("NÚMEROS IGUAIS")

elif num1 < num2:
   print("PRIMEIRO É MAIOR")

else:
   num2 > num1
  
print("SEGUNDO É MAIOR")
