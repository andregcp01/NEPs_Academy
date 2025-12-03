# entrada invidiual
A = input()
A = int(A)

# múltiplas entradas
B = input().split()
# tamanho de B
L = len(B)
# primeiro índice
N = L - L
# o programa ficou bugando no primeiro loop, eu acho que tem que dar alguma valor a S (soma) antes de começar o while
S = 0

# enquanto de "N" até chegar ao tamanho de L
while N < L:
    BN = int(B[N]) # como uma lista é string, ele não identifica como um número, então eu converti o índice em inteiro
    S = S + BN
    N = N + 1

# total das múltiplas entradas (S) mais a entrada individual (A)
T = A + S
#print(T)

# lembrando que essa questão eu fiz sem querer e a resposta na verdade é "S" após o último loop
print(S)