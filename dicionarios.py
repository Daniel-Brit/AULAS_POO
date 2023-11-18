notas =[85, 92, 88, 85, 74, 90, 74, 88, 92]
from collections import Counter

def calcular_nota(notas):
    if len(notas) == 0:
        return None
    media = sum(notas) / len(notas)
    notas_ordenadas = sorted(notas)
    meio = len(notas_ordenadas) // 2
    if len(notas_ordenadas) % 2 == 0:
        mediana = (notas_ordenadas[meio - 1] + notas_ordenadas[meio]) / 2
    else:
        mediana =  notas_ordenadas[meio]
    
    contagem_notas = Counter(notas)
    moda = [nota for nota, contagem in contagem_notas.items() if contagem == max(contagem_notas.values())]
    estatisticas = {
        'media': media,
        'mediana': mediana,
        'moda': moda
    }

    return estatisticas

notas = [85, 92, 88, 85, 74, 90, 74, 88, 92]
estatisticas = calcular_nota(notas)
print(estatisticas)