def ordenar_sem_repeticoes(tupla_strings):
    strings_ordenadas = sorted(set(tupla_strings))
    return tuple(strings_ordenadas)

tupla_original = ("banana", "maçã", "laranja", "banana", "uva")
tupla_ordenada_sem_repeticoes = ordenar_sem_repeticoes(tupla_original)
print(tupla_ordenada_sem_repeticoes)