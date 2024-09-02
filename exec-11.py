#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa de R$ 700,00 para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.


print("Quantidade de carros vendidos no mês:")
carros_vendidos = int(input())

print("Valor total de vendas:")
vendas_total = float(input())

print("Valor do salario fixo mensal:")
salario_fixo = float(input())

extra_bonus_por_carro_vendido = carros_vendidos * 700
bonus_percentual = (5/100) * vendas_total

Salario_final = salario_fixo + extra_bonus_por_carro_vendido + bonus_percentual

print("Salario final:" + str(Salario_final))
