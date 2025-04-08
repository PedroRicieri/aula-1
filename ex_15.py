quantidade = int(input("Quantos números você vai digitar? "))
contador = 0 

for num in range(quantidade):
    numero = float(input("Digite um número: "))
    contador += numero

media = contador / quantidade

print(f"A média dos números é: {media}")