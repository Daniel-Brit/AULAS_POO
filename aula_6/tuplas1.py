def elementos_pares(tupla):
    return tuple(x for x in tupla if x % 2 == 0)

tupla_original = (1, 2, 3, 4, 5)
tupla_pares = elementos_pares(tupla_original)
print(tupla_pares)