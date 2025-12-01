# texto interativo
print("Um belo dia alguns alunos e professores foram pessear na serra. A cabine do bondinho só aguenta 50 pessoas.")
print("Sabendo que, os alunos não podem ir sozinhos e que pelo menos 1 professor deve ir com eles durante o passeio,")
print("você deve fazer um programa que receba as entradas A (alunos) e P (professores) respeitando a  restrição:")
print("1 <= A <= 50")
print("1 <= P <= 50")

# entradas
A = input()
P = input()

# conversões das entradas
A = int(A)
P = int(P)

# A = int(input())
# B = int(input())

# adicionado a varáivel T, total máximo permitido no bodinho
T = A + P

# o total deve ser 49, pois pelo menos 1 professor deve ir a viagem com os alunos e 1 alunos deve ir com os professores
if 1 <= A <= 49 and 1 <= P <= 49 and T <= 50:
    print("Tudo OK! Está dentro da capacidade permitida e respeitou a restrição!\n")
else:
    print("Vixe meu brodinha, assim não dá, reorganizem os grupos!\n")