# Lista de temperaturas
temperaturas = []

# Dias da semana
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

contador = 0

print("Digite a temperatura registrada para cada dia da semana:")

while contador < 7:
    entrada = input(f"{dias[contador]}: ").replace(",", ".").strip()
    if entrada.replace(".", "", 1).isdigit():
        temp = float(entrada)
        temperaturas = temperaturas + [temp]  # sem usar append
        contador += 1
    else:
        print("Digite uma temperatura válida (ex: 23.5)")

# Cálculos
maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / 7

# Exibir resultados
print("\nResultado da semana:")
print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")
print(f"Média semanal: {media:.2f}°C")

# Dias com temperatura acima da média
print("\nDias com temperatura acima da média:")
indice = 0
while indice < 7:
    if temperaturas[indice] > media:
        print(f"{dias[indice]}: {temperaturas[indice]}°C")
    indice += 1
