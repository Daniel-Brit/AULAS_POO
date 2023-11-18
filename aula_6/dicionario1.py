def pais_com_maior_populacao(dicionario):
    if not dicionario:
        return None

    pais_maior_populacao = max(dicionario, key=dicionario.get)
    return pais_maior_populacao

dicionario_populacoes = {"Brasil": 211.8, "China": 1400.5, "Índia": 1366.4}
pais_maior_populacao = pais_com_maior_populacao(dicionario_populacoes)
print(pais_maior_populacao)