#Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.
print("Qual o valor do salario fixo mensal do funcionario?")
salario_fixo = float(input())

print("Qual o valor de vendas do mes do funcionario?")
valor_vendas_mes = float(input())

comissao1_extra = (3/100) * valor_vendas_mes
extra_ref_vendas = valor_vendas_mes - 1500
comissao2_extra = (5/100) * extra_ref_vendas
