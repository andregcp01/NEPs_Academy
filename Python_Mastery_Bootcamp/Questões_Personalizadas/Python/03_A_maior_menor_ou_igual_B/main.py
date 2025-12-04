# entrada de dados
A = input("Primeiro número, A = ")
B = input("Segundo número, B = ")

# conversões, aqui é melhor transformá-las em float mesmo, pois 1.1 é maior do que 1
A = float(A)
B = float(B)

print("")
# se A é diferente de B
if A > B:
    print("{0:.2f} > {1:.2f}. A é maior do que B!".format(A, B))
    print("Logo, se A > B, eles são diferentes!\n")
elif A < B:
    print("{0:.2f} < {1:.2f}. A é menor do que B!".format(A, B))
    print("Logo, se A < B, eles são diferentes!\n")
# se A não é maior ou menor que B, então A é igual a B
else:
    print("{0:.2f} = {1:.2f}. A é igual a B!\n".format(A, B))