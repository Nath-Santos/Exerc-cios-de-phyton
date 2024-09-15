#40) Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 

#- Se quantidade <= 5 o desconto será de 2%
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#- Se quantidade > 10 o desconto será de 5%

def calculo_do_total(nome_produto,quantidade_adquirida, preco_unitario):
total_produto = quantidade_adquirida * preco_unitario

if quantidade_adquirida <= 5:
   desconto = total_produto * 0.02
elif quantidade_adquirida <= 10:
     desconto = total_produto * 0.03
    else:
        desconto = total_produto * 0.05

valor_tt_p_pagamento = total_produto - desconto

return total_produto, desconto, valor_tt_p_pagamento

nome_produto = "Produto"
quantidade_adquirida = 8
preco_unitario = 10.0

total_produto, desconto, total_a_pagar = calculo_do_total(nome_produto, quantidade_adquirida, preco_unitario)

print(f"Produto: {nome_produto}")
print(f"Quantidade adquirida: {quantidade_adquirida}")
print(f"Preço unitário: {preco_unitario}")
print(f"Total_produto: {total_produto}")
print(f"Desconto: {desconto}")
print(f"Valor_tt_p_oagamento: {valor_tt_p_pagamento}")

