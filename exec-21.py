#Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte
print("JOGO DE XADREZ")
print("Hora de inicio da partida:")
hora_inicio = int(input())

print()

print("Hora de termino da partida:")

hora_final = int(input())
print()

tempo = hora_final - hora_inicio
print()
if tempo <=0:
   tempo <+24
   
print()
print(f"Duração do Jogo de xadrez {tempo} horas")
