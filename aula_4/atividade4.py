def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

while True:
    try:
        numero = int(input("Digite um número entre 1 e 10000 (ou 0 para sair): "))
        if numero == 0:
            print("Programa encerrado.")
            break
        elif 1 <= numero <= 10000:
            if is_primo(numero):
                print(f"{numero} é um número primo.")
            else:
                print(f"{numero} não é um número primo.")
        else:
            print("Por favor, digite um número entre 1 e 10000.")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")