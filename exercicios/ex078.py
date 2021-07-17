"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
"""

valores = list()
menor = maior = 0
print('='*50)
print(f'{"PREENCHENDO A LISTA":^50}')
print('='*50)
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c + 1}º valor: ')))
    if c == 0:
        menor = maior = valores[c]
    elif menor > valores[c]:
        menor = valores[c]
    elif maior < valores[c]:
        maior = valores[c]

print('='*50)
print(f'{"INFORMAÇÕES":^50}')
print('='*50)
menorPos = []
maiorPos = []
# Se declarar lista1 = lista2 = [] criasse uma ligação em vez de duas listas iguais
for pos, v in enumerate(valores):
    if v == menor:
        menorPos.append(pos)
    if v == maior:
        maiorPos.append(pos)
print(f'Valores na lista: {valores}')
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for pos, v in enumerate(menorPos):
    if pos + 1 == len(menorPos):
        print(v)
    else:
        print(v, end=' ')

print(f'O maior valor digitado foi {maior} na(s) posição(ões) ', end='')
for pos, v in enumerate(maiorPos):
    if pos + 1 == len(maiorPos):
        print(v)
    else:
        print(v, end=' ')

print('='*50)
