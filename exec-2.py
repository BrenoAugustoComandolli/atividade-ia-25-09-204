from sympy import Eq, symbols, solve

# Definindo a variável
x = symbols('x')

# Definindo a equação
equacao = Eq(x**3 - 9*x, 0)

# Resolvendo a equação para encontrar as raízes
raizes = solve(equacao, x)

# Exibindo as raízes
print("As raízes da equação são:", raizes)