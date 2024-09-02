#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa de R$ 700,00 para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.


Valor_fixo_salario_mensal = (input("digite o valor do salario: "))

Valor_fixo_comissão = input("digite o valor fixo da comissao: ")

Valor_de_Carros_Vendidos= input("digite o valor de carros vendidos:")

Valor_vendas_carros= float(input("digite o percentual sobre as vendas de carros (de 0 a 5): "))

print("O valor final do salário com as comissões é de,Valor_fixo_salario_mensal* (1+Valor_fixo_comissão) * (1+Valor_vendas_carros))
      

