#Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.
time1 = str(input('Digite o nome do primeiro time: '))
time2 = str(input('Digite o nome do segundo time: '))

num_gols_tm1 = int(input('Digite o número de gols do {}:'.format(time1)))

num_gols_tm2 = int(input('Digite o número de gols do {}:'.format(time2)))

if num_gols_tm1 > num_gols_tm2:
   print('{} Vencedor'.format(time1))

elif num_gols_tm2 > num_gols_tm1:
     print('{} Vencedor'.format(time2))

else:
     print("Empate")
