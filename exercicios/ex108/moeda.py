def aumentar(n=0, porcentagem=0):
    nv = n * (1 + porcentagem/100)
    return nv


def diminuir(n=0, porcentagem=0):
    nv = n * (1 - porcentagem/100)
    return nv


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')
