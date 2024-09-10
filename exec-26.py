#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.
print("Controle de Estoque")

print("Quantidade atual do produto")
quant_atual = int(input())

print("Quantidade máxima do produto")
quant_maxima = int(input())

print("Quantidade mínima do produto")
quant_minima = int(input())

quant_media = (quant_maxima + quant_minima) / 2

print("Quantidade media do produto em estoque:" + str(quant_media))
