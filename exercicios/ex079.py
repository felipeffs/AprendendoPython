"""
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""

valores = []
c = total = 0
while True:
    for c in range(c, total):
        while True:
            a = int(input(f' -> '))
            if a in valores:
                print('\033[:31mEste valor já está na lista! Digite outro!\033[m')
                print('\033[:35m-\033[m'*50)
            else:
                valores.append(a)
                print('\033[:32mValor Adicionado!\033[m')
                print('\033[:35m-\033[m'*50)
                break
        # acrescentar valor ao c quando for a ultima repetição
        if c == total - 1:
            c += 1
    print('='*50)
    while True:
        quant = str(input('\033[:34mDeseja adicionar quantos números? \033[m'))
        if quant.isdigit():
            quant = int(quant)
            break
    print('='*50)
    if quant == 0:
        break
    total += quant

print(f'Você digitou os valores: {sorted(valores)}')
