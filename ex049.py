n = int(input('Digite um número inteiro: '))

print('='*20)
print('> Tabuada do {}'.format(n))
for c in range(1, 11):
    print('\t{} X {} = {}'.format(n, c, n * c))
print('='*20)
