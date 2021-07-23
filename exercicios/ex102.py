"""
Crie um programa que tenha um função fatorial() que receba dois parâmetros: o
primeiro que indique o número a calcular e o outro chamado show, que será um valor
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
do fatorial.
"""


def fatorial(n=1, show=False):
    """
        Calcula o fatorial de um número.
    :param n: O número a ser calculado, caso não seja informado o valor será 1.
    :param show: Mostrar ou não a conta, caso não seja informado o valor será False.
    :return: O fatorial de n.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
    print(f)


fatorial(5, True)
help(fatorial)
