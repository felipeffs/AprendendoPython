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
