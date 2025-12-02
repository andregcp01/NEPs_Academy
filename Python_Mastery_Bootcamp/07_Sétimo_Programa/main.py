L = [] # comando que gera listas
print(type(L)) # tipo da variável

# exemplo de uma lista
A = [1, 3, 5, 7]
print(A)

# uma lista pode conter variáveis de todos os tipos, variáveis inteitas, decimais e até strings
B = [2, 12 , 2025.2, "9h52min" ]
print(B)

# para adicionar "valores" ao final da lista, a gente usa esse comando
B.append("9h55min")
print(B)

# comando para "escolher" o valor que você quer que apareça, vai de 0 (zero) até n - 1 (óbvio, porque começa do zero)
print(B[2]) # vai aparecer o 3º valor, no caso 2025.2

# comando para "alterar" determinado valor da lista
B[4] = "10h02min"
print(B)

# comando para "acessar o último valor" da lista
print(B[-1])

# comando para "deletar determinado valor" da lista
del B[3] # o horário de "9h52min" será apagado
print(B)