#40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 

#- Se quantidade <= 5 o desconto será de 2%
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#- Se quantidade > 10 o desconto será de 5%

def calculo_do_total(nome_produto, quant_produto, preco_produto):
total_produto = quant_produto * preco_produto

if quant_produto <= 5:
   desconto = total_produto * 0.02
elif quant_produto <= 10:
     desconto = total_produto * 0.03
    else:
     desconto = total_produto * 0.05

valor_tt_p_pagamento n= total_produto - desconto

return total_produto, descontovalor_tt_p_pagamento

nome_produto = "Produto"
quantidade_adquirida = 8
preco_unitario = 10.0

total_produto, desconto, total_a_pagar = calculo_do_total(nome_produto, quantidade_adquirida, preco_unitario)
