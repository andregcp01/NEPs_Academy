# quantidades de questões da prova
A = int(input())

# questões marcadas pelo aluno
B = input().split()

# gabarito das questões
C = input().split()

# número de acertos
D = 0

# comando para "juntar as letras das questões"
B = "".join(B)
C = "".join(C)

for i in range(A):
    # se o índice de B = índice de C, acerto + 1
    if B[i] == C[i]:
        D = D + 1

print(D)