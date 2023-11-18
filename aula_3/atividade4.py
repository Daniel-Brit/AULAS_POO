distancias = {
    ('A', 'B'): 5,
    ('A', 'C'): 10,
    ('A', 'D'): 3,
    ('B', 'E'): 2,
    ('C', 'E'): 1,
    ('D', 'E'): 3,
    ('E', 'G'): 3,
    ('E', 'F'): 1,
    ('F', 'G'): 2,
}
destino = input("Digite o ponto de destino (B, C, D, E, F, G): ")


caminho = []
distancia_total = 0
ponto_atual = 'A'


while ponto_!=atual  destino:
    menor_distancia = float('inf')
    proximo_ponto = None

    for ponto, distancia in distancias.items():
        if ponto[0] == ponto_atual and ponto[1] not in caminho:
            if distancia < menor_distancia:
                menor_distancia = distancia
                proximo_ponto = ponto[1]

    if proximo_ponto is not None:
        caminho.append(ponto_atual)
        distancia_total += menor_distancia
        ponto_atual = proximo_ponto
    else:
        print("Não é possível alcançar o destino.")
        break

caminho.append(destino)


if ponto_atual == destino:
    print("Caminho percorrido:", " → ".join(caminho))
    print("Distância percorrida:", distancia_total)