from functools import reduce

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

numeros = [1, 2, 3, 4, 5]

triplicados = list(map(lambda x: x * 3, numeros))
print("Triplicado:", triplicados)

dobrados = list(map(lambda x: x * 2, numeros))
print("Dobrados:", dobrados)

pares = list(filter(lambda x: x > 6, dobrados))
print("Maiores de 6:", pares)

soma_total = reduce(subtracao, pares)
print("Soma dos pares:", soma_total)