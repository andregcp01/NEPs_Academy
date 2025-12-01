# texto interativo
print("Olá meu caramarada, eu posso dizer a você se seu número é positivo, negativo ou nulo.\n")

# entrada
X = input("Por gentileza, escreva seu número, X = ")

# conversão
X = int(X)

if X > 0 : # se
    print("Seu número é positivo! Pois {0} > 0.\n".format(X))
elif X < 0: # senão, se
    print("Seu número é negativo! Pois {0} < 0\n".format(X))
else: # senão
    print("Seu valor é nulo! Pois {0} = 0.\n".format(X))

#despedida interativa
print("Até a próxima meu camarada!")