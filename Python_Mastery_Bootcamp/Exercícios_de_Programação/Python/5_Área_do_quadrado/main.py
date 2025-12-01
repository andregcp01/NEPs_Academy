# texto interativo
print("Para descorbrirmos a Área do Quadrado (L²), precisamos do comprimento de seu lado:\n")

# entrada
L = input("L = ")

# conversão da entrada para um número inteiro
L = int(L)
# L = int(input()), resumo

# cálculo da área (m²)
A = L * L

# resultado
print("Seu quadrado tem {0} m²!\n".format(A))