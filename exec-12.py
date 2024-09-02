#12) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo): 

#C5=F - 329

F = float(input("digite a temperatura em Fahrenheit:"))

C = (F - 32) * ( 5 / 9)

print("temperatura em Celsius igual a:", C)
