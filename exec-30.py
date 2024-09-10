#Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.
print("Escreva o 1º numero")
num1 = float(input())

print("Escreva o 2º numero")
num2 = float(input())

print("Escreva o 3º numero")
num3 = float(input())

valores = [num1, num2, num3]

valores.sort()
  
print("Seguem os números em ordem crescente:" + str(valores))
