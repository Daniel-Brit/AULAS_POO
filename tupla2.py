def elementos_pares(tupla):
    nova_tupla = tuple(x for x in tupla if x % 2 == 0)
    return nova_tupla

tupla_original = (1, 2, 3, 4, 5)
nova_tupla = elementos_pares(tupla_original)
print(nova_tupla)  