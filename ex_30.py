import random

# Lista de participantes
participantes = []

print("Digite os nomes dos participantes do sorteio.")
print("Digite 'fim' para encerrar.\n")

while True:
    nome = input("Nome do participante: ").strip()
    if nome.lower() == "fim":
        break
    if nome != "":
        participantes = participantes + [nome]  # adicionando sem append

# Verifica se a lista não está vazia
if participantes:
    vencedor = random.choice(participantes)
    print(f"\nO vencedor do sorteio é: {vencedor}")
else:
    print("\nNenhum participante foi cadastrado. Sorteio cancelado.")
