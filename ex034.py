s = float(input('Salário do funcionário: R$'))

if s > 1250:
    s = s * 1.1
else:
    s = s * 1.15

print('O novo salário é {:.2f}'.format(s))
