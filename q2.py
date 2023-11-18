def q2():
    equipe1 =input("Digite o nome da equipe: ")
    equipe2 =input("Digite o nome da equipe: ")
    placar1 = int(input(f"Digite o resuldado do primeiro jogo entre a {equipe1} x {equipe2}: "))
    placar2 = int(input(f"Digite o resultado do segundo jogo entre a {equipe1} x {equipe2}: "))

    pontos_equipe1 = 0
    pontos_equipe2 = 0

    if placar1 > placar2:
        pontos_equipe1 += 3 
    if placar2 > placar1:
        pontos_equipe2 += 3
    else:
        pontos_equipe1 += 1
        pontos_equipe2 += 1

    TotalDePontos_equipe1 = placar1 + placar2
    TotalDePontos_equipe2 = placar1 + placar2

    if pontos_equipe1 > pontos_equipe2 or TotalDePontos_equipe1 > TotalDePontos_equipe2:
        vencedor = f"{equipe1} venceu o campeonato com {pontos_equipe1} pontos e {TotalDePontos_equipe1} gols."
    elif pontos_equipe2 > pontos_equipe1 or TotalDePontos_equipe2 > TotalDePontos_equipe1:
        resultado = f"{equipe2} venceu o campeonato com {pontos_equipe2} pontos e {TotalDePontos_equipe2} gols."
    else:
        print("O campeonato terminou em empate com pontos e gols iguais.")
        Penaltis_equipe1 = int(input(f"Digite o número de gols na cobrança de pênaltis para {equipe1}: "))
        Penaltis_equipe2 = int(input(f"Digite o número de gols na cobrança de pênaltis para {equipe2}: "))

    if Penaltis_equipe1 > Penaltis_equipe2:
            resultado = f"{equipe1} venceu a cobrança de pênaltis por {Penaltis_equipe1} - {Penaltis_equipe2}."
    elif Penaltis_equipe2 > Penaltis_equipe1:
            resultado = f"{equipe2} venceu a cobrança de pênaltis por {Penaltis_equipe2} - {Penaltis_equipe1}."
    else:
            resultado = "A cobrança de pênaltis também terminou em empate. O campeonato permanece empatado."
    print(resultado)



