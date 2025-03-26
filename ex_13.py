nota = float(input("Digite a primeira nota: "))

if nota >= 7:
    print("O aluno está aprovado!")
elif 5 <= nota <= 6.9:
    print("O aluno está de recuperação.")
else:
    print("O aluno está reprovado.")