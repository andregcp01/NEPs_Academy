# texto interativo
print("Uma jovem pesquisadora chamada Luiza Solange decidiu encontrar a fórmula")
print("que fazia o huehuehue do brasileiro ser tão engraçado na internet, então")
print("ela, juntamente com seu pupilo Anderson, fizeram diversas análises e, por fim,")
print("chegaram a conclusão de que, quando a quantidade de VOGAIS mais a quantidade")
print("de H superam, ou atingem, os 75 por cento do comprimento da risada, a risada")
print("é considerada engraçada. Faça um programa que imprima S, quando a risada for")
print("engraçada, e N, quando a risada não for engraçada.")
print("Restrições: se não há vogal é N")

# dados de entrada
A = input()

# tamanho de A
B = len(A)

# comando que separa as entradas
A = list(A)

# variável que irá verificar a quantidade de vogais
C = 0

# variável que irá verificar a quantidade de H
D = 0

for i in range(B):
# solução elegante.. descobri depois.. a minha foi essa
#    if A[i] == ['a', 'e', 'i', 'o', 'u']:
#        C = C + 1
    if A[i] == 'a' or A[i] == 'e' or A[i] == 'i' or A[i] == 'o' or A[i] == 'u':
        C = C + 1
    elif A[i] == 'h':
        D = D + 1

print(C)
print(D)

# cálculo da risada engraçada
E = C + D
print(E)
print(B)

if C == 0:
    print("N")
else:
    if E / B >= 0.75:
        print("S")
    else:
        print("N")
