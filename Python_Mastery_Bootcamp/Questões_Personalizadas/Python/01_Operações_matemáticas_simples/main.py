# entrada de dados
A = input("Primeiro número, A = ")
B = input("Segundo número, B= ")

# conversão das entradas
A = int(A)
B = int(B)

print("")
# utilizaçao do .format para puxar dados
print("Seu primeiro número foi {0} e o segundo foi {1}".format(A, B))

# agora as operações, para pequenas operações o .format é elegante, pois não há necessidade de implementar outra variável
print("")

# soma, X + Y
print("A soma de {0} + {1} = {2}".format(A, B, A + B))

# subtração, X - Y
print("A subtração de {0} - {1} = {2}".format(A, B, A - B))

# multiplicação, X * Y
print("A multiplicação de {0} * {1} = {2}".format(A, B, A * B))

#divisão, X / Y, o comando "Z:.2f" indica a quantidade de algarismos que a gente quer que apareça após a vírgula
print("A divisão de {0} / {1} = {2:.2f}\n".format(A, B, A / B))