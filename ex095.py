jogador = dict()
jogadores = list()
gols = list()

while True:
    jogador.clear()
    print('=' * 50)
    while True:
        quant = str(input('Quantos jogadores deseja cadastrar? ')).strip()
        if quant.isdigit():
            quant = int(quant)
            break
        print('\033[31mQuantidade Inválida! Digite novamente.\033[m')
    print('=' * 50)
    if quant == 0:
        break
    for q in range(0, quant):
        while True:
            jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
            nome = jogador['Nome'].replace(' ', '')
            if nome.isalpha():
                break
            print('\033[31mNome Inválido! Digite novamente.\033[m')
        print('—'*50)
        while True:
            quant = str(input(f'Quantas partidas {jogador["Nome"]} jogou? ')).strip()
            if quant.isdigit():
                quant = int(quant)
                break
            print('\033[31mQuantidade Inválida! Digite novamente.\033[m')
        print('—'*50)
        total = 0
        gols.clear()
        for partida in range(0, quant):
            while True:
                g = str(input(f'Quantos gols na partida {partida + 1}? ')).strip()
                if g.isdigit():
                    gols.append(int(g))
                    total += int(g)
                    print('—'*50)
                    break
                print('\033[31mQuantidade inválida! Digite novamente.\033[m')
        jogador['Gols'] = gols[:]
        jogador['Total'] = total
        jogadores.append(jogador.copy())
# print(jogadores)

print(f'{"COD":<3} {"NOME":<19} {"GOLS":<19} {"TOTAL":<5}')
print('-'*50)
for pos, j in enumerate(jogadores):
    print(f'{pos:<3} {j["Nome"]:<19} {str(j["Gols"]):<19} {j["Total"]:<5}')
print('-' * 50)

while True:
    while True:
        cod = str(input('Mostrar dados de qual jogador? (999 para parar) ')).strip()
        if cod.isdigit():
            cod = int(cod)
            if cod < len(jogadores) or cod == 999:
                break
            else:
                print('\033[31mNão existe nenhum jogador com esse código cadastrado! '
                      'Digite novamente.\033[m')
        else:
            print('\033[31mCódigo Inválido! Digite novamente.\033[m')
    if cod == 999:
        break
    print('-' * 50)
    print(f' — LEVANTAMENTO DO JOGADOR/A {jogadores[cod]["Nome"].upper()}')
    for jogo, gols in enumerate(jogadores[cod]["Gols"]):
        print(f'\t No jogo {jogo + 1} fez {gols} gols.')
    print('-' * 50)

print(f'\n{"-PROGRAMA FINALIZADO-":^50}')
