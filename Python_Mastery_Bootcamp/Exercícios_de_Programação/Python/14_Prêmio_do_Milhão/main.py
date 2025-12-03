# quantidades de dias
A = int(input())

# contador de dias
B = 0

# acessos por dia
C = 0

# total de acessos
D = 0

# aqui é uma repetição, se "D" não atingir a quantidade de acessos
# necessárias, a gente vai lançar uma nova linha, ou seja, um novo
# input A
for i in range(A):
    C = C + int(input())
    D = D + C
    B = B + 1
    # aqui o programa vai verificar se ele já atingiu o objetivo, a
    # quantidade de visualizações
    if D >= 1000000:
        break

# o que a gente realmente quer saber é quantos dias se passaram até 
# atingir o objetivo, então o importante aqui é o "B"
print(B)