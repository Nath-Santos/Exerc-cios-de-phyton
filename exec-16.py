#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
maca =int(input("Quantidade de macas:"))

if maca < 12

soma=maca*1.30

print("Valor a ser pago compra menor que 12 unidades:",soma)

else:

soma=maca*1.00

print("Valor a ser pago compra menor que 12 unidades:",soma)
