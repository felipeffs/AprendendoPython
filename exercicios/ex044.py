"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
— Á vista dinheiro/cheque: 10% de desconto
— Á vista no cartão: 5% de desconto
— Em até 2x no cartão: preço normal
— 3x ou mais no cartão: 20% de juros
"""

print('{:▰^42}'.format('LOJA TEVENIDO'))

p = float(input('\nValor do produto: '))
f = int(input('Forma de pagamento:\n'
              '0: Á vista ou cheque\n'
              '1: No cartão\n'))

if f == 0:
    n = p * 0.9
    print('O produto de R${:.2f} fica por R${:.2f} á vista'.format(p, n))
elif f == 1:
    c = int(input('Em quantas vezes? '))
    if c == 1:
        n = p * 0.95
        print('O produto de R${:.2f} fica por R${:.2f} á vista no cartão'.format(p, n))
    elif c <= 2:
        print('O preço do produto continua por R${:.2f} em {}x no cartão'.format(p, c))
    else:
        n = p * 1.2
        print('O preço de R${:.2f} fica por R${:.2f} em {}x no cartão'.format(p, n, c))

print('▰'*37)
