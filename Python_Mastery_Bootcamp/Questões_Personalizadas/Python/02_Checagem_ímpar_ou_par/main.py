# entrada
A = input("Escreva seu número, A = ")
A = int(A) # apenas NÚMEROS INTEIROS podem ser pares ou ímpares

# variáveis necessárias
B = float(A / 2)  # aqui ele vai fazer uma divisão, pois todo número par é divisivel por 2
C = int(B) # aqui o C vai converter B em inteiro

print(B)
print(C)

print("")
# vai fazer a verificação
if B == C:
    print("{0} é par!\n".format(A))
# aqui ele vai fazer a checagem com zero, apesar de zero ser nulo, algumas literaturas o consideram par
elif B == 0:
    print("{0} é par!\n".format(A))
# aqui se o número não for 0 nem par, ele é ímpar
else:
    print("{0} é impar!\n".format(A))