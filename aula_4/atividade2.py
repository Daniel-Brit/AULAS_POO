def pesquisa_satisfacao():
    print("Pesquisa de Satisfação no Atendimento da Farmácia")
    print("Opções de respostas: INSATISFEITO, SATISFEITO, NÃO QUERO RESPONDER")

    num_respostas = int(input("Quantos usuários irão responder à pesquisa? "))

    contador_insatisfeito = 0
    contador_satisfeito = 0
    contador_nao_responder = 0

    for i in range(num_respostas):
        resposta = input(f"Resposta do usuário {i + 1}: ").strip().upper()

        if resposta == "INSATISFEITO":
            contador_insatisfeito += 1
        elif resposta == "SATISFEITO":
            contador_satisfeito += 1
        elif resposta == "NÃO QUERO RESPONDER":
            contador_nao_responder += 1
        else:
            print("Resposta inválida. Por favor, escolha entre INSATISFEITO, SATISFEITO ou NÃO QUERO RESPONDER.")

    percentual_insatisfeito = (contador_insatisfeito / num_respostas) * 100
    percentual_satisfeito = (contador_satisfeito / num_respostas) * 100
    percentual_nao_responder = (contador_nao_responder / num_respostas) * 100

    print("\nResultados da Pesquisa:")
    print(f"INSATISFEITO: {percentual_insatisfeito:.2f}%")
    print(f"SATISFEITO: {percentual_satisfeito:.2f}%")
    print(f"NÃO QUERO RESPONDER: {percentual_nao_responder:.2f}%")

pesquisa_satisfacao()

