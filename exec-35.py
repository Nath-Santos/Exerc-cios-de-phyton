#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90. 
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90. 
print("Nº de litros Vendidos: ")
quant_litros = int(input())

print("Código do combustivel, sendo A = ALCOOL E G = GASOLINA")
cod_comb = str(input())

if cod_comb == "Alcool":
   cod_comb = "A"
   
else:    
     if cod_comb == "Gasolina":
        cod_comb = "G"
   
if quant_litros > 20 and cod_comb == "A":
   pag_preco_final = (quant_litros * 2.90) - ((5 / 100) * quant_litros)
   
elif quant_litros > 20 and cod_comb == "G":
     pag_preco_final = (quant_litros * 3.30) - ((6 / 100) * quant_litros)
elif quant_litros <= 20 and cod_combustivel == "A":
     pag_preco_final = (quant_litros * 2.90) - ((3 / 100) * quant_litros)
else:
     if quant_litros <= 20 and cod_comb == "G":
        pag_preco_final = (quant_litros * 3.30) - ((4 / 100) * quant_litros)

print("O valor do preco final para pagamento: R$" + str(pag_preco_final)) 
