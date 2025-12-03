V = 0

# novo comando "enquanto"
while V < 5:
    print(V)
    V = V + 1
print("")

# novo comando "para"
for i in [1, 2, 3]:
    print("Para i in [1, 2, 3]")
    print(i)
print("")

# agora adicionando os números 4 e 5 "a lista i"
for i in [1, 2, 3, 4, 5]:
    print("Para i in [1, 2, 3, 4, 5]")
    print(i)
print("")

# comando para não precisar escrever sempre a lista inteira
for j in range(1, 5): # note que a lista não "engloba" o 5, ela só vai até 4, ou seja é sempre o último número -1
    print("Para j in range(1, 5)")
    print(j)
print("")

for j in range(1, 6): #agora ele irá até 5
    print("Para j in rage(1, 6)")
    print(j)
print("")

# podemos "incrementar valores" ao range(ínicio, fim, incremento)
for j in range(0, 20, 4):
    print(j)
print("")

# o comando range não é uma lista, como veremos abaixo
R = range(0, 10) # nós podemos simplificar a escrita, quando começamos do número 0, escrevendo apenas range(10)
print(R)
print("")

# para transformarmos o comando range em lista, devemos introduzi-lo dentro de uma list
R = range(10)
print(list(R))
print("")