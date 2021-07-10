n = int(input('Digite um número inteiro: '))
primo = ''
if n == 1:
    print('{} não é um número primo'.format(n))
else:
    for c in range(2, n):
        if n % c == 0:
            primo = ' não'
    print('{}{} é um número primo'.format(n, primo))
