def aumentar(n=0, porcentagem=0, f=False):
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


def resumo(p=0, a=0, r=0):
    print('—'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('—'*40)
    print(f'{"Preço analisado:":<30}{moeda(p):<10}')
    print(f'{"Dobro do preço:":<30}{dobro(p, True):<10}')
    print(f'{"Metade do preço:":<30}{metade(p, True):<10}')
    print(f'{f"{a}% de aumento:":<30}{aumentar(p, a, True):<10}')
    print(f'{f"{r}% de redução:":<30}{diminuir(p, r, True):<10}')
    return True
