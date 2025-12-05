# dados de entrada
A = input()

# tamanho de A
B = len(A)

# comando que separa as entradas
A = list(A)

# lista das vogais
C = []

for i in range(B):
    if A[i] == 'a' or A[i] == 'e' or A[i] == 'i' or A[i] == 'o' or A[i] == 'u':
        C.append(A[i])

print(C)

# lista C ao contrário
D = C[::-1]

if C == D:
    print("S")
else:
    print("N")