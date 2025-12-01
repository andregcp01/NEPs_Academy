# entrada de dados
A = input("Primeiro número, A = ")
B = input("Segundo número, B = ")

# conversões das entradas
A = int(A)
B = int(B)

# ou simplesmente
# A = int(input())
# B = int(input())

# soma de A + B
C = int(A + B)

# média de A + B
D = int(C / 2)

print("A média inteira de ({0} + {1}) / 2 = {2}\n".format(A, B, D))