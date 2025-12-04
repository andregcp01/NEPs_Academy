# texto interativo
print("Malu deve levar a escola: lapiseira, borracha e caderno")
print("O que Malu deve levar a escola?")

# entradas de dados
A = input().split()

print("")
# note que, para a entrada está correta, pois agora é uma lista ou string as palavras devem estar entre [] (cochetes)
# se não aplicarmos uma vírgula entre as palavras elas se concatenarão, em string se usa ' simples entre os valores
if A == ['lapiseira', 'borracha', 'caderno']:
    print("Você acertou!\n")
else:
    print("Você errou!\n")
    print("Sua lista foi: {0}".format(A))

# também existe a possibilidade de ao invés de escrever os valores, nós atribuimos o valor a uma variável, acho que
# o programa fica mais elegante
R = ['lapiseira', 'borracha', 'caderno']
print("A lista esperada: {0}\n".format(R))