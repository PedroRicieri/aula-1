# Lista para armazenar compromissos como tuplas: (data, descrição)
agenda = []

print("=== Agenda de Compromissos ===")

while True:
    print("\n1 - Adicionar compromisso")
    print("2 - Exibir todos os compromissos")
    print("3 - Buscar compromissos por data")
    print("4 - Exibir compromissos ordenados por data")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        data = input("Digite a data (formato AAAA-MM-DD): ").strip()
        descricao = input("Descrição do compromisso: ").strip()

        if len(data) == 10 and data[4] == "-" and data[7] == "-":
            agenda = agenda + [(data, descricao)]  # adicionando sem append
            print("Compromisso adicionado.")
        else:
            print("Formato de data inválido. Use o formato AAAA-MM-DD.")

    elif opcao == "2":
        if agenda:
            print("\nCompromissos cadastrados:")
            for item in agenda:
                print(f"{item[0]} - {item[1]}")
        else:
            print("Nenhum compromisso cadastrado.")

    elif opcao == "3":
        busca = input("Digite a data para buscar (AAAA-MM-DD): ").strip()
        encontrou = False
        for item in agenda:
            if item[0] == busca:
                print(f"{item[0]} - {item[1]}")
                encontrou = True
        if not encontrou:
            print("Nenhum compromisso encontrado nessa data.")

    elif opcao == "4":
        if agenda:
            # Ordenar usando comparação direta de strings (datas no formato AAAA-MM-DD)
            ordenada = []
            i = 0
            while i < len(agenda):
                menor = agenda[i]
                j = i + 1
                while j < len(agenda):
                    if agenda[j][0] < menor[0]:
                        menor, agenda[j] = agenda[j], menor
                    j += 1
                ordenada = ordenada + [menor]
                i += 1

            print("\nCompromissos ordenados por data:")
            for item in ordenada:
                print(f"{item[0]} - {item[1]}")
        else:
            print("Agenda vazia.")

    elif opcao == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida.")