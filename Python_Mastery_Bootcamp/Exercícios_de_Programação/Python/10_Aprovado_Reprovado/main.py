# texto interativo
print("Lá na escola do José Camelo, os alunos são aprovados caso tenham média superior ou igual a 7,")
print("eles ficam de recuperação se a média for menor do que 7 e maior ou igual a 4 e se os alunos")
print("obtiverem notas menores do que 4 são automaticamente reprovados.")

# no exercício as entradas estão bugadas, pois ele quer que as notas fiquem na mesma linha, então devemos consertar primeiro as entradas
# A = float(input()) (original)
# B = float(input()) (original)

# foi eu que fiz essa entrada? não, eu copiei a entrada do exercício do Flíper, só ajustei para float
A, B = map(float, input().split())

# variável Média:
M = (A + B) / 2

# solução
if M < 4:
    print("Garotinho você brincou demais! Você está reprovado!\n")
elif 4 <= M < 7:
    print("Não desanime, mas não deixe de estudar! Você está de recuperação!\n")
else:
    print("Parabéns você foi aprovado!\n")

print("Final do semetre 2025.2")