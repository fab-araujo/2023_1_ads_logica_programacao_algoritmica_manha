turmas = input("Digite o total de turmas: ")
turmas = int(turmas)

total_alunos = 0

for i in range(turmas):
    n_alunos = input("Digite o total de alunos: ")
    n_alunos = int(n_alunos)
    while n_alunos > 40:
        print("Número de alunos inválido!")
        n_alunos = input("Digite o total de alunos: ")
        n_alunos = int(n_alunos)
    total_alunos = total_alunos + n_alunos

print(total_alunos/turmas)