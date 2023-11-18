inicio = float(input('Digite o começo:'))
fim = float(input('Digite o fim:'))

terceiro_valor = float(input('Digite o valor:'))

if inicio <= terceiro_valor <= fim:
    print('está dentro do intervalo')
else:
    if terceiro_valor <= inicio:
        print('está na parte inferior')
    else:
        print('está na parte superior')
