# Lista de compras vazia
lista_compras = []

while True:
    print("\n--- Menu ---")
    print("1 - Adicionar item")
    print("2 - Exibir lista")
    print("3 - Remover item")
    print("4 - Finalizar programa")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        item = input("Digite o nome do item: ")
        lista_compras = lista_compras + [item]  # adiciona item sem usar append

    elif escolha == "2":
        print("\n Itens na lista:")
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")

    elif escolha == "3":
        item_remover = input("Digite o nome do item que deseja remover: ")
        if item_remover in lista_compras:
            indice = lista_compras.index(item_remover)
            lista_compras = lista_compras[:indice] + lista_compras[indice+1:]  # remove sem .remove()
            print(f"Item '{item_remover}' removido com sucesso.")
        else:
            print("Item não encontrado na lista.")

    elif escolha == "4":
        print("\n Lista final de compras:")
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i}. {item}")
        print("\nPrograma finalizado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
