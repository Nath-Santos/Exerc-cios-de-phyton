# 41) Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula abaixo e escrever o conceito do aluno de acordo com a tabela de conceitos mais abaixo:

# Média_de_aproveitamento = (N1 + (N2 * 2) + (N3 * 3)) / 7 

# A atribuição de conceitos obedece a tabela abaixo:

# A > = 9,0
# B > = 7,5 e < 9,0
# C > = 6,0 e < 7,5
# D < 6,0

print("Escreva a nota da 1ª Avaliação:")
N1 = float(input())

print("Escreva a nota da 2ª Avaliação:")
N2 = float(input())

print("Escreva a nota da 3ª Avaliação:?")
N3 = float(input())

Média_de_aproveitamento = (N1 + (N2 * 2) + (N3 * 3)) / 7

if Média_de_aproveitamento >= 9:
    Conceito = "A"
    print(f"Media de aproveitamento: {Média_de_aproveitamento:.2f}")
    print(f"Conceito: {Conceito}")
elif Média_de_aproveitamento >= 7.5 and Média_de_aproveitamento < 9:
    Conceito = "B"
    print(f"Media de aproveitamento: {Média_de_aproveitamento:.2f}")
    print(f"Conceito: {Conceito}")
elif media_aproveitamento >= 6 and Média_de_aproveitamento < 7.5:
    Conceito = "C"
    print(f"Media de aproveitamento: {Média_de_aproveitamento:.2f}")
    print(f"Conceito: {Conceito}")
else:
    Conceito = "D"
    print(f"Media de aproveitamento: {Média_de_aproveitamento:.2f}")
    print(f"Conceito: {Conceito}")
