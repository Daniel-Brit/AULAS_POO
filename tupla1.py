def strings_ordenadas_sem_repeticoes(tupla):
    nova_tupla = tuple(sorted(set(tupla)))
    return nova_tupla

# Exemplo de uso:
tupla_original = ("banana", "maçã", "laranja", "banana", "uva")
nova_tupla = strings_ordenadas_sem_repeticoes(tupla_original)
print(nova_tupla)  # Saída: ("banana", "laranja", "maçã", "uva")