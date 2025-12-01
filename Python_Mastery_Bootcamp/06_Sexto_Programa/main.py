# Expressões booleanas:
# ---------------------
# menor que, <
# ---------------------
# maior que, >
# ---------------------
# menor ou igual, <=
# ---------------------
# maior ou igual, >=
# ---------------------
# igual, ==
# ---------------------
# diferente, !=
# ---------------------
# e, and
# ---------------------
# ou, or
# ---------------------

# OBS: Apenas um "=", significa receber. Por exemplo, A = B, A receberá o valor armazenado em B

A = 5
B = 10
C = 5
D = "{0}".format(C) # D está recebendo o valor de C e o alterando para string (frase)

if A < B:
    print("Verdadeiro")
else:
    print("Falso")

if A > B:
    print("Verdadeiro")
else:
    print("Falso")

if A == C:
    print("Verdadeiro")
else:
    print("Falso")

if A == 5:
    print("Verdadeiro")
else:
    print("Falso")

if A == "5": # string 5, ou seja, uma frase não um número
    print("Verdadeiro")
else:
    print("Falso")

if D == "5": 
    print("Verdadeiro")
else:
    print("Falso")

if A == C and A < B:
    print("Verdadeiro")
else:
    print("Falso")

if A < B or A != C:
    print("Verdadeiro")
else:
    print("Falso")

if A > B or A == C:
    print("Verdadeiro")
else:
    print("Falso")