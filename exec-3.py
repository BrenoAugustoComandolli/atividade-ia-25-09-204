from functools import reduce

def soma(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]

dobrados = list(map(lambda x: x * 2, numeros))
print("Dobrados:", dobrados)

pares = list(filter(lambda x: x % 2 == 0, dobrados))
print("Pares:", pares)

soma_total = reduce(soma, pares)
print("Soma dos pares:", soma_total)