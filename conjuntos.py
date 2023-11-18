def novo_conjunto(conjunto1, conjunto2):
    resultado = conjunto1.intersection(conjunto2)
    return resultado

conjunto1 = {1, 2, 7, 8, 9}
conjunto2 = {1, 2, 10, 11, 12}
resultado = novo_conjunto(conjunto1, conjunto2)
print(resultado)
