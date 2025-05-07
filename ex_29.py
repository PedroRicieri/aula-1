# Lista de alunos presentes
presentes = []

# Cadastro de presença
print("Digite os nomes dos alunos presentes.")
print("Digite 'fim' para encerrar o cadastro.\n")

while True:
    nome = input("Nome do aluno: ").strip()
    if nome.lower() == "fim":
        break
    if nome != "":
        presentes = presentes + [nome]  # adiciona sem usar append

# Total de alunos presentes
total = len(presentes)
print(f"\nTotal de alunos presentes: {total}")

# Buscar por um aluno específico
buscar = input("Deseja verificar se um aluno estava presente? (sim/não): ").strip().lower()

if buscar == "sim":
    nome_busca = input("Digite o nome do aluno: ").strip()
    if nome_busca in presentes:
        print(f"{nome_busca} estava presente.")
    else:
        print(f"{nome_busca} não está na lista de presença.")
