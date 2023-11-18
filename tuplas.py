lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
def contar_elementos_unicos(lista):
    contagem = {}
    resultado = []

    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1

    for elemento in lista:
        if contagem[elemento] > 0:
            resultado.append((elemento, contagem[elemento]))
            contagem[elemento] = 0

    return resultado

lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
resultado = contar_elementos_unicos(lista)
print(resultado)