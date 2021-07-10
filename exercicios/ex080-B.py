valores = []
pos = 0
for c in range(0, 5):
    a = int(input('-> '))
    if c == 0 or a > valores[-1]:
        valores.append(a)
        pos = c
    else:
        for p, v in enumerate(valores):
            if a < v:
                valores.insert(p, a)
                pos = p
                break
    print(f'\033[34mAdicionado na posição {pos} da lista!\033[m')
print(f'Os valores digitados em ordem foram {valores}')
