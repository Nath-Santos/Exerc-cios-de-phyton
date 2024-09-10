#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

print("Dados da conta do cliente")
print("Nº da conta:")
numero_da_conta = int(input())

print("Saldo da conta:")
saldo_conta = float(input())

print("Débito:")
debito = float(input())

print("Crédito:")
credito = float(input())

saldo_atual_da_conta = float(saldo_conta - debito + credito)
print("saldo atual da conta:")
print(saldo_atual_da_conta)

if saldo_atual_da_conta >= 0:
   print("Saldo positivo")

else:("Saldo negativo")



