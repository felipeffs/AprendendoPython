quant = num = resp = maior = menor = soma = 0
while resp != 'N':
    quant += 1
    num = float(input('Digite um número: '))
    if quant == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    resp = str(input('Deseja continuar digitando valores? [S/N]\n')).upper().strip()[0]
media = soma / quant
print('{} números foram digitados\n'
      'Média: {:.2f}\n'
      'Menor Valor: {:.2f}\n'
      'Maior Valor: {:.2f}\n'.format(quant, media, menor, maior))
