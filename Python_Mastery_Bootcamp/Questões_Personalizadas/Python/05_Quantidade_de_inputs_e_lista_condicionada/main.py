# texto interativo
print("José Camelo foi ao mercantil comprar: arroz, batata, carne, cenoura e feijao")

# entrada de dados
A = input("Quantos itens José Camelo comprou? A = ")
A = int(A)

# quantidade de itens
Q = 5

# lista de compras
L = []

print("")
# primeira análise, para adicionar a quantidade de linhas extras
if A == Q:
    print("Certo! Mas o que ele comprou?\n")
    for i in range(A):
        I = input()
        # irá adicionar o novo input a lista
        L.append(I)
        print(L)
    print("")
    # lista de José Camelo
    J = ['arroz', 'batata', 'carne', 'cenoura', 'feijao']
    # análise dos itens
    if L == J:
        print("Muito bem! Você acertou novamente!\n") 
    else:
        print("Você errou! Observe com atenção a ordem das compras!\n")
        print("A sua lista = {0}".format(L))
        print("A lista esperada = {0}\n".format(J))
else:
    print("Você errou! Leia o texto novamente!\n")