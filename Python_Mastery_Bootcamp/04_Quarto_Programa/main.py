A = input() #entrada de dados
print(A)

X = input() #entrada do valor de X
Y = input() #entrada do valor de Y
print(X + Y) #porque o restultado deu 65? porque todo input é string, por isso devemos declarar variáveis, igual a abaixo

X = int(X) #conversão de X para um número inteiro
Y = int(Y) #conversão de Y para um número inteiro
print(X + Y) # agora o resultado é 11, pois o programa entende que X e Y são numerais inteiros

a, b = input().split() #o split "quebra" a linha em vários pedaços

a = int(a) #conversão de a
b = int(b) #conversão de b

print(a + b)