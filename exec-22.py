#A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
print("Considerando o valor do salario de: R$ 2000")
salario_mes = 2000
hrs_trab_por_sem = 40 

print("Quant horas trabalhadas na semana:")
hrs_trab_no_mes= input(int(4*40))

print("V$ salario por hora trab:")
valor_salario_hora = input(float(2000 / 160))

hora_extra = valor_salario_hora * 0,50
extra_percentual = (50/100) + valor_salario_hora

Salario_final = valor_salario_hora + extra_percentual * horas_trab_do_mes

print("Salario_final:" + str(Salario_final))
