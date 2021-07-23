"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


def voto(nascimento):
    from datetime import datetime
    idade = datetime.now().year - nascimento
    if idade <= 15:
        if idade == 1:
            return f'Com {idade} ano\033[33m não pode votar.\033[m'
        else:
            return f'Com {idade} anos\033[33m não pode votar.\033[m'
    elif idade < 18 or idade > 70:
        return f'Com {idade} anos o voto é\033[34m facultativo.\033[m'
    else:
        return f'Com {idade} anos o voto é\033[32m obrigatório.\033[m'


def leiaInt(msg='', dado='Número', f=False):
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
        if f:
            erro = f'{dado.capitalize()} inválida!'
        else:
            erro = f'{dado.capitalize()} inválido!'
        print(f'\033[31m[!] - {erro} Digite novamente.\033[m')
    return int(numero)


print('-'*50)
print(voto(leiaInt('Em que ano você nasceu? ', 'ano')))
