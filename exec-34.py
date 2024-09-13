#dado o algoritmo, faça um teste de mesa  que complete o quadro  a seguir:
print("Valor de X: ")
X = int(input())

print("Valor de Y: ")
Y = int(input())


Z = (X * Y) + 5

if    Z <= 0:
      resposta = 'A'

elif  Z <= 100:
      resposta = 'B'

else:
      resposta = 'C'
print(f'O valor de Z é: (Z) / resposta: {resposta}')

