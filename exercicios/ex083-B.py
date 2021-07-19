"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta.
"""

exp = str(input('Digite uma expressão: '))
pilha = []
for p in exp:
    if p == '(':
        pilha.append('(')
    elif p == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\033[34mExpressão Correta\033[m')
else:
    print('\033[31mExpressão Incorreta\033[m')
