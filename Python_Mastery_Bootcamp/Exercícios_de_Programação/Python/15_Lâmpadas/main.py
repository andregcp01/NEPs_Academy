# input que representa a quantidade de vezes que os interruptores 1 e 2 foram acesos
A = input()
A = int(A)
# A = int(input())

# input que representa a ordem que os interruptores foram, ou não, acesos
B = input().split()

# valor da inicial da primeira lâmpada
L1 = 0

# valor inicial da segunda lâmpada
L2 = 0

for i in range(A):
    # esse seria o if "numérico", mas eu quero responder como texto, pois os números sempre são os mesmos
    # if int(B[i]) == 1:

    # aqui ele vai ser texto, se ler 1, ele acende ou desliga L1
    if B[i] == '1':
        L1 = L1 ^ 1 # L1 ^ 1 ou L ^= 1, um comando "binário", achei uma solução muito boa para casos de falso ou verdadeiro

    # esse seria o elif "numérico"
    # elif int(B[i]) == 2:

    # da mesma forma que o if, se ele for um texto igual a 2, ele ascende ou desliga ambas as lâmpadas
    elif B[i] == '2':
        L1 = L1 ^ 1 # L1 ^= 1
        L2 = L2 ^ 1 # L2 ^= 1

print(L1)
print(L2)