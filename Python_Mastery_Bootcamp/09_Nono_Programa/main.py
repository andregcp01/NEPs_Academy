# strings aceitam tanto aspas duplas quanto aspas simples
s1 = "Olá, NEPs Academy!"
s2 = 'Olá, NEPs Academy!'

print(s1)
print(s2)

L = len(s1)
print("O comprimento de s1 e s2 = {0}".format(L))
print("")

# note que em uma string separa as letras, espaços e símbolos
for i in range(L):
    print(s1[i])
print("")

# também podemos podemos imprimir índices específicos
print(s1[0])  # a letra O
print(s2[-1]) # a letra y, último índice
print("")

# também podemos substituir as strings por outras
print(s1)
print(s2)
print("")

print(s1.replace("NEPs Academy", "José Camelo"))
print(s2.replace("NEPs Academy", "Luiza Solange"))
print("")

# em strings o split junta as palavras, e pode até mesmo, a eliminá-las, como podemos ver abaixo
print(s2.split())
print(s2.split("NEPs"))
print("")

# comandos para fixar caixa alto, baixa, ou mostrar a frase original
print(s1.upper())
print(s1.lower())
print(s1.title())
print("")

# outro exemplo para passar valores contidos na string
palavra = "Olá!"

for letra in palavra: # passa por cada letra da string
    print(letra) # imprime a letra em uma linha separada
print("")

# outro exemplo para "fatiar" strings, porém retornando um nova string
s3 = "Olá, Anderson e Malu"
print(s3)
L3 = len(s3)
print(L3)
print("")

substring = s3[5:20] # esse é comando para "fatiar"
print(substring)
print("")

substring = s3[:14] # tudo atrás do caractere 14
print(substring)
print("")

substring = s3[14:] # tudo depois do caractere 14
print(substring)
print("")

# também podemos fazer adições a string, também conhecido como incrementos
s4 = "Olá Luiza Solange, José Camelo"
print(s4)
L4 = len(s4)
print(L4)
print("")

print(s4[::2]) # a string foi percorrida de 2 em 2 posições
print("")

# fazer strings ao contrário, um comando MUITO importante na hora de resolver esses exercícios malucos
print(s4[::-1])
print("")