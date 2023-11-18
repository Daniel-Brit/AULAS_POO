while True:
    temperatura_str = input("Digite a temperatura atual (ou um valor negativo para sair): ")
    temperatura = float(temperatura_str)

    if temperatura < 0:
        print("Programa encerrado.")
        break

    if temperatura < 15:
        print("Aqui não é o RN")
    elif 16 <= temperatura <= 25:
        print("Pense num frio")
    elif 26 <= temperatura <= 30:
        print("Temperatura normal e super agradável")
    elif 31 <= temperatura <= 35:
        print("Tá quente pra danado")
    else:
        print("Calor da muléstia!")