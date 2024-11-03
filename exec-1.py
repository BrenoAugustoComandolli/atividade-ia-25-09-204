from sympy import symbols, Eq, solve
x = symbols('x') 
eq = Eq(x**2 - 4, 0)
sol = solve(eq)
print(sol)