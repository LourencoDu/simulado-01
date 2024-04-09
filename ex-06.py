tempo_foco = float(input("Entre com a quantidade de tempo do período de foco, em minutos: "))
if(tempo_foco >= 25 and tempo_foco <= 45):
  print(f"{tempo_foco} minutos é um tempo aceitável!")
else:
  print(f"{tempo_foco} minutos é não um tempo aceitável!")