print(f'{"Programa=Tabuada":=^40}')

while True:
    print('='*40)
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n < 0:
        print('\033[:34mPrograma Tabuada Finalizado\033[m')
        break
    for c in range(1, 11):
        print(f'{f"{c} X {n} = {c * n}":^34}')
