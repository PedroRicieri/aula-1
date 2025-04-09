# Lista para armazenar as notas
notas = []

while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip()

    if entrada.lower() == "fim":
        break

    # Verifica se é um número (permitindo ponto decimal)
    entrada_formatada = entrada.replace(".", "", 1)  # remove UM ponto para validar como número
    if entrada_formatada.isdigit():
        nota = float(entrada)
        notas = notas + [nota]  # adicionando sem usar append
    else:
        print("Entrada inválida. Digite apenas números (ex: 7.5) ou 'fim'.")

# Resultados
if len(notas) == 0:
    print("\nNenhuma nota foi cadastrada.")
else:
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)

    print("\n📊 Resultados:")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Média das notas: {media:.2f}")
