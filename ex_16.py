numero = float(input("Digite um número: "))

resultado = 1
for fatorial in range(numero + 1):
    resultado *= fatorial
print(f"O fatorial de {numero} é {resultado}")