numero = int(input('Digite um número:'))

if numero < 0:
    print('numero negativo pode ser fatorado')
elif numero == 0:
    print('o fatorial de 0 é 1')
else:
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
        print(f'o faotiral de {numero} é {resultado}:')
