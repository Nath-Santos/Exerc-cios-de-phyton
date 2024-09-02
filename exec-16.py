#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("Quantidade de macas compradas:")
macas_compradas = int(input())

print("Valor unitario de macas para compra de 6 unidades:")
valor_unitario = float(input())

valor_total_compra_6_unidades = macas_compradas * valor_unitario 

print("valor total compra 6unidades:" + str(valor_total_compra_6_unidades))




print("Quantidade de macas compradas:")
macas_compradas = int(input())

print("Valor unitario de macas para compra de 12 unidades:")
valor_unitario = float(input())

valor_total_compra_12_unidades = macas_compradas * valor_unitario 

print("valor total compra 12unidades:" + str(valor_total_compra_12_unidades))
