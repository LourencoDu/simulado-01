numero = int(input("Entre com o número que deseja saber a tabuada: "))
print(f"Tabuada de {numero}:")
for multiplicador in range(1, 11):
  print(f"{numero} x {multiplicador} = {numero * multiplicador}")