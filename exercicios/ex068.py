from random import randint
vitorias = 0
print('-='*25)
print(f'{"!Jogo de Par ou Ímpar!":=^50}')
while True:
    print('-=' * 25)
    pc = randint(0, 10)
    n = int(input('Diga um valor: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 50)
    t = pc + n
    print(f'Jogou {n} e o computador {pc}. Total deu {t}', end='')
    if t % 2 != 0:
        print(' [IMPAR]')
        if tipo == 'P':
            break
    else:
        print(' [PAR]')
        if tipo == 'I':
            break
    vitorias += 1
    print('Você VENCEU!!!')
    print('-=' * 25)
    print(f'{"Próximo round":^50}')
print(f'Você PERDEU!!')
print('-='*25)
print(f'Foram {vitorias} vitórias consecutivas')
