"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o
sort()). No final, mostre a lista ordenada na tela.
"""

valores = []
maior = pos = 0
for c in range(0, 5):
    a = int(input('-> '))
    if c == 0 or a > maior:
        valores.append(a)
        maior = a
        pos = c
    else:
        for p, v in enumerate(valores):
            if a < v:
                valores.insert(p, a)
                pos = p
                break
    print(f'\033[34mAdicionado na posição {pos} da lista!\033[m')
print(f'Os valores digitados em ordem foram {valores}')
