# texto interativo
print("Vamos lá meu joinha, aperte os botões do Flíper para mexer a bolinha\n")
print("Lembando que eles só recebem os valores 0 e 1, 0 para mover a esquerda e 1 para mover a direita")

# entrada (totalmente copiada do exercício)
A, B = map(int, input().split())

# se a entrada A = 0, a bolinha sempre irá para a direção C
if (A == 0 and B == 0) or (A == 0 and B == 1):
    print("A bolinha saiu pela saída C!\n")

# se a entrada A = 1, temos duas possibilidades:
# se B = 0 a bolinha vai para a saída B
if A == 1 and B == 0:
    print("A bolinha saiu pela saída B!\n")

# se B = 1, a bolinha vai para a saída A
if A == 1 and B == 1:
    print("A bolinha saiu pela saída A!\n")