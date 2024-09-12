#Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.
print("Time 1")
num_gols_tm1 =int(input())

print("Time 2")
num_gols_tm2 =int(input())


if num_gols_tm1 > num_gols_tm2 and num_gols_tm2 < num_gols_tm1:
   soma = num_gols_tm1 + num_gols_tm2

elif num_gols_tm2 < num_gols_tm1 and num_gols_tm1 < num_gols_tm1:
   soma = num_gols_tm2 + num_gols_tm1

else:
   soma = num_gols_tm1 + num_gols_tm2
  

print("O vencedor da partida é:" +str(soma))
