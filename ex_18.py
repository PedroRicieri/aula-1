entrada = input("Digite os números separados por espaço: ")

numeros = []
for num in entrada.split():
    numeros.append(int(num))

tamanho = 0
for _ in numeros:
    tamanho += 1

for i in range(tamanho):
    for j in range(0, tamanho - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista ordenada:", numeros)
