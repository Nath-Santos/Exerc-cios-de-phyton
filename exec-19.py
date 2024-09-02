#Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

na = int(input("Digite o primeiro valor:"))
nb = int(input("Digite o segundo valor:"))

maior = na
if nb > na and nb > na:
    maior > nb
    
if nb > na and nb > na:
    menor = na

print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")

#verificar se a solução abaixo está correta também, na primeira não está imprindo o nº maior e o nº menor


na = int(input("Digite o primeiro valor:"))
nb = int(input("Digite o segundo valor:"))
nc = int(input("Digite o terceiro valor:"))
maior = na
if nb > na and nb > nc:
    maior = nb
if nc > na and nc >= nb:
    maior = nc
menor = na
if nb < nc and nb < na:
    menor = nb
if nc <= nb and nc < na:
    menor = nc
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")
