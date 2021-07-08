from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
maior = menor = 0
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior número é {max(numeros)} e o menor é {min(numeros)}')
