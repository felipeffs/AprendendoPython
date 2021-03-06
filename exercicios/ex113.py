"""
Reescreva a função leiaInt() que fizemos no exercício 104, incluindo agora a
possibilidade da digitação de um número de tipo inválido. Aproveite e crie também
uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg=''):
    while True:
        try:
            a = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO: O valor digitado não é um número inteiro. Por favor, digite novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO: Nenhum valor foi informado.\033[m')
            return 0
        else:
            return a


def leiaFloat(msg=''):
    while True:
        try:
            a = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO: O valor digitado não é um número real. Por favor, digite novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERRO: Nenhum valor foi informado.\033[m')
            return 0
        else:
            return a


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro lido foi {n1} e o real foi {n2:.2f}')
