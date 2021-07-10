def ficha(nome='desconhecido', gols=0):
    if nome == str():
        nome = 'desconhecido'
    else:
        nome = nome.title()
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


def leiaIntp(msg='', dado='Número', f=False):
    """
        Um input que só aceita e continua a execução caso receba um número inteiro
    :param msg: Mensagem que será exibida antes de pedir o input
    :param dado: o tipo de valor lido para personalizar a mensagem de erro - "[!] 'dado' inválido! Digite novamente."
    :param f: se o tipo for do gênero feminino coloque True (o valor padrão é False).
    :return: O número inteiro digitado.
    """
    while True:
        numero = str(input(msg)).strip()
        if numero.isdigit():
            break
        elif numero == str():
            numero = int()
            break
        if f:
            erro = f'{dado.capitalize()} inválida!'
        else:
            erro = f'{dado.capitalize()} inválido!'
        print(f'\033[31m[!] - {erro} Digite novamente.\033[m')
    return int(numero)


ficha(str(input('Nome do Jogador: ')), leiaIntp('Número de gols: ', 'quantidade de gols', True))
