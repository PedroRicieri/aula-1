palavra = input("Digite uma palavra: ")
vogais = ['a']
quantidade = 0
for letra in palavra:
    quantidade += 1
print(f"A palavra '{palavra}' possui {quantidade} vogais.")