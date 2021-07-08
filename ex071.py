print('=' * 50)
print(f'{"BANCO NARVAL":^50}')
print('=' * 50)
valor = ''
while not valor.strip().isdigit():
    valor = input('Valor a ser sacado: R$')
valor = int(valor)
qNota = nota = c = 0
print('=' * 50)
while valor != 0:
    if c == 0:
        nota = 50
    elif c == 1:
        nota = 20
    elif c == 2:
        nota = 10
    elif c == 3:
        nota = 1
    else:
        break
    c += 1
    qNota = valor // nota
    valor -= qNota * nota
    if qNota != 0:
        print(f'Total de {qNota} cédulas de R${nota}')
print('=' * 50)
print('Volte Sempre!')