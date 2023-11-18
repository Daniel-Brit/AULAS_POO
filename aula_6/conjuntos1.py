def elementos_comuns(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
elementos_comuns_resultado = elementos_comuns(conjunto1, conjunto2)
print(elementos_comuns_resultado)