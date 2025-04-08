atual = input("Digite os itens da lista de compras atual (separados por vírgula): ")

lista_compras = []
for item in atual.split(","):
    lista_compras.append(item.strip())

faltando = input("Digite os itens que estão faltando (separados por vírgula): ")

for item in faltando.split(","):
    item = item.strip()
    if item not in lista_compras:
        lista_compras.append(item)

print("Lista de compras otimizada:", lista_compras)
