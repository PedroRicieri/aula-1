senha_correta = "1234"
tentativas = 0
acesso_liberado = False

while tentativas < 3:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso liberado!")
        acesso_liberado = True
        break
    else:
        print("Senha incorreta.")
        tentativas += 1

if not acesso_liberado:
    print("Acesso bloqueado. Número de tentativas excedido.")
