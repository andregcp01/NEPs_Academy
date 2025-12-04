# quantidade de valores da lista
#N = int(input())

# lista com os valores
#C = list(map(int, input().split()))

# variáveis de estado das lâmpadas (False = apagado / 0, True = acesa / 1)
#L1 = False
#L2 = False

#for i in C:
    # se um valor na lista for 1, apertamos o disjuntor 1
#    if i == 1:
        # inverte o valor apenas de L1
#        L1 = not L1
    # se um valor na lista for diferente de 1, no caso pode ser 2
#    elif  i != 1:
        # invertemos o valor de L1 e L2
#        L1 = not L1
#        L2 = not L2

# aqui acontece a conversão, verdadeiro e para 1 e falso para 0
#CL1 = 1 if L1 else 0
#CL2 = 1 if L2 else 0

#print(CL1)
#print(CL2)

# quantidade de valores da lista
N = int(input())

# lista com valores 1 ou 2, 1 ascende ou apaga L1, 2 faz o "contrário com ambas as lâmpadas"
I = input().split()

# valor inicial da lâmpada 1
L1 = 0

# valor inicial da lâmpada 2
L2 = 0

# aqui acontecerá uma interação com todos os índices presente na lista N
for i in range(N): 
    # se o índice for 1, a L1 apaga ou ascende
    if int(I[i]) == 1:
        if L1 == 0:
            L1 = 1
        else:
            L1 = 0
    # quando for outro valor != 1, no caso 2, ela irá alterar tanto L1 quanto L2 para seus respectivos "contrários"
    else:
        # quando L1 for 0, ele irá torná-la 1
        if L1 == 0:
            L1 = 1
        # quando L1 for 1, ele irá torná-la 0
        else:
            L1 = 0
        # quando L2 for 0, ele irá torná-la 1
        if L2 == 0:
            L2 = 1
        # quando L2 for 1, ele irá torná-la 0
        else:
            L2 = 0

# essa é a resolução padrão do exercício, eu achei que caiu bem, pois a resposta foi simples, apesar de aparentar ser confuso as
# análises, a questão já tem o principal para um noobzinho (eu), que é o que? receber um valor e adicioná-lo a uma lista na mesma
# linha, existem algumas questões que a gente usa isso muito, por isso essa questão é importante (na minha opinião)
print(L1)
print(L2)