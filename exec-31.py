#Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.

print("Escreva o valor do lado A")
valorA  = float(input())

print("Escreva o valor do lado B")
valorB = float(input())

print("Escreva o valor do lado C")
valorC = float(input())

if  valorA < valorB + valorC and valorB < valorC + valorA and valorC < valorA + valorB:
    print("As medidas formam um triangulo")

else:
     ("As medidas não formam um triangulo")
