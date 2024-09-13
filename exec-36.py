#Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.
print("Digite a idade do 1º homem:?")
idade_homem1 = int(input())

print("Digite a idade do 2º homem:?")
idade_homem2 = int(input())

print("Digite a idade da 1ª mulher?")
idade_mulher1 = int(input())

print("Digite a idade da 2ª mulher?")
idade_mulher2 = int(input())

homem_idad_velho = max(idade_homem1, idade_homem2)
homem_idad_novo = min(idade_mulher1, idade_mulher2)

mulher_idad_velha = max(idade_mulher1, idade_mulher2)
mulher_idad_nova = min(idade_mulher1, idade_mulher2)

Valor_soma_idades = homem_idad_velho + mulher_idad_nova
Resultado_produto_idades = homem_idad_novo * mulher_idad_nova
        
print("Resultado da soma das idades do Homem velho com a Mulher Nova: " + str(Valor_soma_idades))
print("Resultado do produto das idades do Homem Novo com a Mulher Velha: " + str(Resultado_produto_idades))
