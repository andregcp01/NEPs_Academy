A = 10
B = 2
C = 5

print("A soma de A e B é", A + B) # dois argumentos

X = 3
Y = 2

print("O valor de X + Y = {}".format(X + Y)) # as {} (chaves) puxam o valor .format(varável1 + variável2)

V1 = 5
v1 = -3

print("O resultado da soma de {0} + {1} = {2}".format(V1, v1, V1 + v1)) # a caixa alta IMPORTA, V1 e v1, são duas coisas diferentes
                                                                        # as {} (chaves) respeitam a ordem das variáveis que criamos

X2 = 4
Y2 = 3

print("O valor da divisão {0} : {1} = {2:.2f}".format(X2, Y2, X2 / Y2)) # o comando {:.2f} limita a quantidade de casas decimais

print("O valor da divisão {0} : {1} = {2:.4f}".format(X2, Y2, X2 / Y2)) # o comando {:.4f} aqui foram 4

nome = "Luiza Solange"
idade = 60

print(f"Olá {nome}! Você tem {idade} anos de idade!") # para "puxar" strings existe a necessidade de "f" antes do texto

print("NEPs", end=" ") # o "end" faz com que o próximo "comando" continue na mesma linha
print("Academy!")