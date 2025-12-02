# texto interativo
print("Olá meu camarada, o texto da questão é bem longo, então, desta vez, não")
print("terá o contexto, ou retextualização, você deverá ver na questão mesmo!\n")

# entradas
P1, C1, P2, C2 = map(int, input().split())
# eu que fiz? não, a questão ja entrega essa entrada para escrever os 4 números na mesma linha

# criação das variáveis
A = P1 * C1
# peso da criança 1 * o comprimento da gangorra 1
B = P2 * C2
# peso da criança 2 * o comprimento da gangorra 2

# solução
if A > B:
    print("A criança está na posição -1!\n")
elif A < B:
    print("A criança está na posição 1!\n")
else:
    print("A criança está na posição 0!\n")