x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))

print("Escolha uma operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Sair")

opcao = int(input("Digite um número e escolha uma operação: "))

if opcao == 1:
    resultado = x + y
    print(f"O resultado de {x} + {y} é igual: {resultado}")
elif opcao == 2:
    resultado = x - y
    print(f"O resultado de {x} - {y} é igual: {resultado}")
elif opcao == 3:
    resultado = x * y
    print(f"O resultado de {x} * {y} é igual: {resultado}")
elif opcao == 4:
    if y != 0:
        resultado = x / y
        print(f"O resultado de {x} / {y} é igual: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitido.")    
else:
    print("Obrigado!")