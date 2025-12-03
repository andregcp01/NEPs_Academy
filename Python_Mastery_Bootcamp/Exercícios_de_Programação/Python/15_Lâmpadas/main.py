# quantidade de valores da lista
N = int(input())

# lista com os valores
C = list(map(int, input().split()))

# variáveis de estado das lâmpadas (False = apagado / 0, True = acesa / 1)
L1 = False
L2 = False

for i in C:
    # se um valor na lista for 1, apertamos o disjuntor 1
    if i == 1:
        # inverte o valor apenas de L1
        L1 = not L1
    # se um valor na lista for diferente de 1, no caso pode ser 2
    elif  i != 1:
        # invertemos o valor de L1 e L2
        L1 = not L1
        L2 = not L2

# aqui acontece a conversão, verdadeiro e para 1 e falso para 0
CL1 = 1 if L1 else 0
CL2 = 1 if L2 else 0

print(CL1)
print(CL2)