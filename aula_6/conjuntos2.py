def palindromos(strings):
    return {string for string in strings if string == string[::-1]}

conjunto_strings = {"arara", "casa", "ovo", "radar"}
palindromos_resultado = palindromos(conjunto_strings)
print(palindromos_resultado)