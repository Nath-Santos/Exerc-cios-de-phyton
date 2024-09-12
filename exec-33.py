#33) Ler dois valores e imprimir uma das três mensagens a seguir:

#‘Números iguais’, caso os números sejam iguais
#‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
#‘Segundo maior’, caso o segundo seja maior que o primeiro.

valor1 = str(input('nome do 1º valor: '))
valor2 = str(input('nome do 2º valor: '))

valor1 = int(input('Digite o número {}:'.format(valor1)))

valor2 = int(input('Digite o número {}:'.format(valor2)))

if valor1 > valor2:
   print('{} O PRIMEIRO É MAIOR'.format(valor1))

elif valor2 > valor1:
     print('O SEGUNDO É MAIOR'.format(valor2))

else:
     valor1 == valor2
     print("NUMEROS IGUAIS")
