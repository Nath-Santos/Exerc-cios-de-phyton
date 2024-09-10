#23) Para o enunciado a seguir foi elaborado um algoritmo em Português Estruturado que contém erros, identifique os erros no algoritmo apresentado abaixo: Enunciado: Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas:

#- para sexo masculino: peso ideal = (72.7 * altura) - 58
#- para sexo feminino: peso ideal = (62.1 * altura) - 44.7

#inicio
#ler nome
#ler sexo
#se sexo = M então
#peso_ideal = (72.7 * altura) - 58
#senão peso_ideal = (62.1 * altura) – 44.7
#fim_se
#escrever peso_ideal
#fim

peso = float(input("Escreva o peso (Kg)? "))
altura = float(input("Escreva a altura (M)? "))
peso_ideal_F = 62.1
peso_ideal_fem = (peso_ideal_F * altura) - 44.7
print("O peso ideal para o sexo Feminino é: {}".format(peso_ideal_fem))

peso_ideal_M = 72.7
peso_ideal_masc = (peso_ideal_M * altura) - 58
print("O peso ideal para o sexo Masculino é: {}".format(peso_ideal_masc))
