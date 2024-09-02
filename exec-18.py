#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

print("Escreva o ano atual:")
ano_atual = int(input())

print("Escreva o seu ano de nascimento:")
ano_nascimento = int(input())

ano_para_votar = ano_atual - ano_nascimento

if ano_para_votar > 18:
    print("VOCE VOTA ESSE ANO.")
elif ano_para_votar < 18:
    print("VOCE NAO VOTA ESSE ANO.")
