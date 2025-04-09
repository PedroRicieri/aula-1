# Começamos com uma lista vazia
alunos = []

# Cadastro de alunos
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar o cadastro): ")
    if nome.lower() == 'sair':
        break
    alunos = alunos + [nome]  # usamos concatenação para adicionar o nome

# Exibir todos os alunos cadastrados
print("\nAlunos cadastrados:")
for aluno in alunos:
    print(f"- {aluno}")

# Perguntar se deseja remover alguém
remover = input("\nDeseja remover algum aluno? (sim/não): ")

if remover.lower() == 'sim':
    nome_remover = input("Digite o nome do aluno que deseja remover: ")
    if nome_remover in alunos:
        index = alunos.index(nome_remover)
        alunos = alunos[:index] + alunos[index+1:]  # removendo sem usar .remove()
        print(f"\nAluno '{nome_remover}' removido com sucesso.")
    else:
        print(f"\nAluno '{nome_remover}' não encontrado na lista.")

# Exibir lista atualizada
print("\nLista final de alunos:")
for aluno in alunos:
    print(f"- {aluno}")