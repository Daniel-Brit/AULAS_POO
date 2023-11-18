def calcular_equacao(a, b, x):
    return a * x + b

num_equacoes = int(input("Quantas equações você deseja calcular? "))

coeficientes_a = []
coeficientes_b = []
valores_x = []

for i in range(num_equacoes):
    a = float(input(f"Digite o valor de 'a' para a equação {i + 1}: "))
    b = float(input(f"Digite o valor de 'b' para a equação {i + 1}: "))
    x = float(input(f"Digite o valor de 'x' para a equação {i + 1}: "))

    coeficientes_a.append(a)
    coeficientes_b.append(b)
    valores_x.append(x)

for i in range(num_equacoes):
    a = coeficientes_a[i]
    b = coeficientes_b[i]
    x = valores_x[i]
    print(f"\nEquação {i + 1}: y = {a}*{x} + {b}")
    y = calcular_equacao(a, b, x)
    print(f"Para x = {x}, y = {y}")