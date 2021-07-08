n = 0
soma = -999
q = -1
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
    q += 1
print('{} foram digitados e a soma de seus valores foi {}'.format(q, soma))
