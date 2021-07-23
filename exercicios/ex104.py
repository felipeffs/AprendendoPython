"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
á função input() do Python, só que fazendo a validação para aceitar apenas um valor
numérico.
Ex:
n = leiaInt('Digite um n')
"""


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


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
