ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))

for c in range(ptermo, ptermo + (10 * razao), razao):
    print(c, end=' ')
