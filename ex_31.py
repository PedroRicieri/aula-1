# Lista de números
numeros = []

# Contador para controlar as 10 entradas
contador = 0

print("Digite 10 números:")

while contador < 10:
    entrada = input(f"Número {contador + 1}: ")
    if entrada.isdigit():
        numero = int(entrada)
        numeros = numeros + [numero]  # adicionando sem append
        contador += 1
    else:
        print("Digite um número válido.")

# Ordenações
ordem_crescente = sorted(numeros)
ordem_decrescente = sorted(numeros, reverse=True)

# Filtrar números pares
pares = []
for n in numeros:
    if n % 2 == 0:
        pares = pares + [n]  # sem usar append

# Exibir resultados
print("\nNúmeros em ordem crescente:", ordem_crescente)
print("Números em ordem decrescente:", ordem_decrescente)
print("Números pares:", pares)
