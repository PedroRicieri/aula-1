# Entrada do valor da conta
valor_conta = float(input("Digite o valor total da conta: "))

# Mostrar opções de gorjeta
print("Escolha a porcentagem da gorjeta:")
print("1 - 10%")
print("2 - 15%")
print("3 - 20%")

# Entrada da escolha do usuário
opcao = input("Digite o número da opção escolhida (1, 2 ou 3): ")

# Determinar porcentagem com base na escolha
if opcao == "1":
    porcentagem = 0.10
elif opcao == "2":
    porcentagem = 0.15
elif opcao == "3":
    porcentagem = 0.20
else:
    print("Opção inválida. Usando 10% por padrão.")
    porcentagem = 0.10

# Calcular gorjeta e total
valor_gorjeta = valor_conta * porcentagem
total_com_gorjeta = valor_conta + valor_gorjeta

# Mostrar resultados
print("Valor da gorjeta: R$", round(valor_gorjeta, 2))
print("Total com gorjeta: R$", round(total_com_gorjeta, 2))
