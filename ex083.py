exp = str(input('Digite um expressão: '))
parenteses = []

for e in exp:
    if e == '(' or e == ')':
        parenteses.append(e)

while True:
    if len(parenteses) > 1 and parenteses[0] == '(':
        if ')' in parenteses:
            parenteses.remove('(')
            parenteses.remove(')')
        else:
            break
    else:
        break

if len(parenteses) == 0:
    print('\033[34mExpressão Correta\033[m')
else:
    print('\033[31mExpressão Incorreta\033[m')
