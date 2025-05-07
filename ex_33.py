# Lista de palavras
palavras = []

contador = 0
print("Digite 10 palavras:")

# Coletar 10 palavras
while contador < 10:
    palavra = input(f"Palavra {contador + 1}: ").strip()
    if palavra != "":
        palavras = palavras + [palavra]
        contador += 1
    else:
        print("Digite uma palavra válida.")

# Criar nova lista com palavras que começam com vogal
vogais = "aeiouAEIOU"
palavras_vogais = []

i = 0
while i < 10:
    if palavras[i][0] in vogais:
        palavras_vogais = palavras_vogais + [palavras[i]]
    i += 1

# Exibir resultados
print("\nLista original:")
print(palavras)

print("\nPalavras que começam com vogal:")
print(palavras_vogais)
