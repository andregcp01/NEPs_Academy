# quantidade de entradas, quantidade de linhas
N = input()
N = int(N)

# lista vazia para armazenar os dados
L = []

# contador de dias
C = 0

# total de acessos
T = 0

# aqui vai ser a repetição e a análise do dados
for i in range(N):
    # V irá receber o valor da nova entrada
    V = int(input())
    # irá adicionar V a lista L
    L.append(V)
    # se o valor de T for menor do que 1000000, ele irá adicionar +1 em C
    if T < 1000000:
        T = T + V
        C = C + 1
        # se o valor T alcançar o valor estimado, ele não adicionará +1 em C
        if T >= 1000000:
            C = C + 0

# quantidade de dias que levaram até atingir o objetivo
print(C)
print(L)