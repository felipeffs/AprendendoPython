from geral import dados


def titulo(msg):
    print('—'*50)
    print(f'{msg:^50}')
    print('—'*50)


def menu(op):
    titulo('MENU PRINCIPAL')
    for c in range(0, len(op)):
        print(f'\033[35m{c+1}\033[m — \033[34m{op[c]}\033[m')
    print('—'*50)
    return dados.leiaInt('\033[32mSua opção: \033[m')
