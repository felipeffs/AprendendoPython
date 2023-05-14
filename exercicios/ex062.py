"""
Melhore o Exercício 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar
0 termos.
"""

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
c = 1

print('PA: ', end='')
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(termo, end=' ')
        termo += razao
        c += 1
    mais = int(input('\nQuer ver mais quantos termos? '))

print('Progressão finalizada com {} termos mostrados'.format(total))
