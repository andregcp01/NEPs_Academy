# texto interativo
print("Um belo dia, Anderson e Malu estavam brincando de par ou ímpar.")
print("Ou seja, cada um escolhia um número e depois era feito a soma.")
print("O vencedor da rodada era aquele, que após declarar sua escolha, a soma resultasse em par ou ímpar.")
print("O Anderson sempre escolhia par e a Malu sempre escolhia ímpar.\n")

# entrada dos dados
A = input("O Anderson jogou, A = ")
B = input("A Malu jogou, B = ")
print("")

# conversão dos dados de entrada
A = int(A)
B = int(B)

# análise se ele resultar num número inteiro C = D, caso contrário o C é decimal (float)
C = (A + B) / 2

D = int(C)

if C != D:
    print("A Malu venceu esta rodada!\n")
else:
    print("O Anderson venceu esta rodada!\n")