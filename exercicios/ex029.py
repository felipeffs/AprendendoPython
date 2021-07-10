"""
Escreva um programa que leia a velocidade de um carro.
Se ela ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

vel = int(input('Velocidade do veículo: '))

if vel > 80:
    valorMulta = (vel - 80) * 7
    print('>>>Você foi multado!!!!<<<<'
          '\nValor a pagar: R${},00'.format(valorMulta))
