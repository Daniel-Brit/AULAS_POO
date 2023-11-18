class No:
    def __init__(self, letra, prox):
        self.letra = letra
        self.prox = prox

lista = [
    No('e', 1), No('h', 2), No('b', 3), No('f', 4), No('a', 5),
    No('i', 6), No('g', 7), No('c', 8), No('d', -1)
]

letras_ordenadas = sorted([no.letra for no in lista if no.letra != 'c'])
print("Letras em ordem alfabética:", ' '.join(letras_ordenadas))

listaSemC = [no for no in lista if no.letra != 'c']
print("Sequência sem a letra 'c':", ' '.join([no.letra for no in listaSemC]))

for no in lista:
    if no.letra == 'c':
        no.letra = 'j'

l = 0
while l != -1:
    print(lista[l].letra, end=' ')
    l = lista[l].prox

'''
 o programa utiliza alocação dinâmica de memória, pois  os objetos do tipo 'No' são criados dinamicamente durante a execução do programa. A lista 
 'lista' permite a manipulação dinâmica dos objetos 'No', e as referências a objetos dinâmicos são armazenadas nela, possibilitando a flexibilidade 
 na manipulação da estrutura de dados.
'''