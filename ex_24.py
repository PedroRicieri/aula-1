senha_atual = 0
executando = True

print("=== Sistema de Atendimento ===")

while executando:
    print("\nOpções:")
    print("1 - Chamar próximo")
    print("2 - Encerrar atendimento")
    
    escolha = input("Digite sua opção: ")
    
    if escolha == "1":
        senha_atual += 1
        print("Chamando senha:", senha_atual)
    elif escolha == "2":
        print("Atendimento encerrado.")
        executando = False
    else:
        print("Opção inválida. Tente novamente.")
