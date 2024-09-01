#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 


Valor_carro_fabrica = float(input("digite o valor do carro: "))

impostos = float(input("digite o reajuste em percentual (de 0 a 45): "))

percentual_distribuidor = float(input("digite o reajuste em percentual (de 0 a 28): "))


print("O valor final do carro para o concumidor é de: ",Valor_carro_fabrica* (1+percentual_distribuidor) * (1+impostos))


















