# texto interativo
print("A Vovó, o Papai e a Malu estavam brincando de zerinho ou um, zerinho é representado pela mão fechada e")
print("um é representado pelo dedo indicador esticado. No zerinho ou um, o vencedor da rodada é aquele que tem")
print("o resultado diferente dos outros.\n")

print("A Vóvó vence se o resultado for 1 0 0, por exemplo")
print("O Papai vence de o resultado for 0 1 0, por exemplo")
print("A Malu vence se o resultado for 1 1 0, por exemplo")
print("O jogo empata quando todos dão o mesmo resultado como 0 0 0, por exemplo\n")

# variáveis
V, P, M = map(int, input().split())
# as entradas da questão

# solução
if (V != P) and (V != M):
    print("A Vovó venceu!\n")
elif (P != V) and (P != M):
    print("O Papai venceu!\n")
elif (M != V) and (M != P):
    print("A Malu venceu!\n")
else:
    print("Essa rodada foi empate!\n")