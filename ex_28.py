# Dicionário para armazenar o estoque
estoque = {}

while True:
    print("\n--- Menu ---")
    print("1 - Adicionar produto")
    print("2 - Buscar produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque completo")
    print("5 - Finalizar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ").strip().lower()
        quantidade = input("Quantidade: ")

        if quantidade.isdigit():
            quantidade = int(quantidade)
            if nome in estoque:
                estoque[nome] += quantidade
            else:
                estoque[nome] = quantidade
            print(f"Produto '{nome}' adicionado com {quantidade} unidades.")
        else:
            print("Quantidade inválida. Digite apenas números.")

    elif opcao == "2":
        nome = input("Digite o nome do produto para buscar: ").strip().lower()
        if nome in estoque:
            print(f"{nome}: {estoque[nome]} unidades em estoque.")
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        nome = input("Produto a atualizar: ").strip().lower()
        if nome in estoque:
            nova_qtd = input("Nova quantidade: ")
            if nova_qtd.isdigit():
                estoque[nome] = int(nova_qtd)
                print(f"Estoque de '{nome}' atualizado para {nova_qtd}.")
            else:
                print("Quantidade inválida.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        print("\nEstoque Atual:")
        if len(estoque) == 0:
            print("Estoque vazio.")
        else:
            for produto, qtd in estoque.items():
                print(f"- {produto}: {qtd} unidades")

    elif opcao == "5":
        print("\nEstoque Final:")
        for produto, qtd in estoque.items():
            print(f"- {produto}: {qtd} unidades")
        print("\nPrograma encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
