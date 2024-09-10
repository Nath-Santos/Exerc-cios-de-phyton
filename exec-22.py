#A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
total_horas_trab_mes = 160

print("digite a quant de hrs trab no mes:")
horas_trab_mes = int(input())

print("digite o valor do salario por hora trabalhada:")
salario_por_hora_trab = float(input())

hora_extra = horas_trab_mes - total_horas_trab_mes
salario_com_extra = ((50/100) * salario_por_hora_trab) * hora_extra
salario_do_mes = horas_trab_mes * salario_por_hora_trab

if horas_trab_mes == total_horas_trab_mes:
    salario_com_extra = salario_do_mes
    print("salario_do_mes: R$ " + str(salario_do_mes))
    print("salario_com_extra: R$ " + str(salario_com_extra))
elif horas_trab_mes > total_horas_trab_mes:
    salario_com_extra = salario_do_mes + salario_com_extra
    print("salario_do_mes: R$ " + str(salario_do_mes))
    print("salario_com_extra: R$ " + str(hora_extra))
    print("salario_com_extra: R$ " + str(salario_com_extra))
else: 
    salario_com_extra = salario_do_mes
    print("salario_com_extra: R$ " + str(salario_com_extra))
