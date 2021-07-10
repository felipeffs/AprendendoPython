from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
maior = menor = 0
print('Os números sorteados foram: ', end='')
for pos, n in enumerate(numeros):
    print(n, end=' ')
    if pos == 0:
        menor = n
        maior = n
    elif menor > n:
        menor = n
    elif maior < n:
        maior = n
print(f'\nO maior número é {maior} e o menor é {menor}')
