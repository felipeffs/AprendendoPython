n = soma = q = 0
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    q += 1
    n = int(input('Digite um número: '))
print('{} foram digitados e a soma de seus valores foi {}'.format(q, soma))
