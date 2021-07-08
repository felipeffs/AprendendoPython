def aumentar(n, porcentagem, f=False):
    nv = n * (1 + porcentagem/100)
    if f:
        nv = moeda(nv)
    return nv


def diminuir(n=0, porcentagem=0, f=False):
    nv = n * (1 - porcentagem/100)
    if f:
        nv = moeda(nv)
    return nv


def dobro(n=0, f=False):
    n *= 2
    if f:
        n = moeda(n)
    return n


def metade(n=0, f=False):
    n /= 2
    if f:
        n = moeda(n)
    return n


def moeda(n=0.0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')
