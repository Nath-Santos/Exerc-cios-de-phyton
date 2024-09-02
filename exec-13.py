#Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:


#media_final = n1 * 2 + n2 * 3 + n3 * 5/10

nota1 = float(input('Primeira nota:'))

nota2 = float(input('Segunda nota:'))

nota3 = float(input('Terceira nota:'))

media_final = (nota1 + nota2 + nota3)*5/10

print("O valor da media final é:", media_final)


