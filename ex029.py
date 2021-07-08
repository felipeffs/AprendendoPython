vel = int(input('Velocidade do veículo: '))

if vel > 80:
    valormulta = (vel - 80) * 7
    print('>>>Você foi multado!!!!<<<<\nValor a pagar: R${},00'.format(valormulta))
