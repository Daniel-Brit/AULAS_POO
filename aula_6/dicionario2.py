def alunos_aprovados(dicionario_notas):
    alunos_aprovados = {}
    for aluno, notas in dicionario_notas.items():
        media = sum(notas) / len(notas)
        if media >= 7.0:
            alunos_aprovados[aluno] = round(media, 2)
    return alunos_aprovados

dicionario_notas = {"Ana": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]}
alunos_aprovados_resultado = alunos_aprovados(dicionario_notas)
print(alunos_aprovados_resultado)