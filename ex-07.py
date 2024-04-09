idade = int(input("Entre com a sua idade: "))
categoria = "Adulto"

if(idade <= 12):
  categoria = "Criança"
elif(idade < 18):
  categoria = "Adolescente"

print(f"Sua categoria: {categoria}")