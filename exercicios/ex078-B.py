"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
"""

valores = list()
print('='*50)
print(f'{"PREENCHENDO A LISTA":^50}')
print('='*50)
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c + 1}º valor: ')))
print('='*50)
print(f'{"INFORMAÇÕES":^50}')
print('='*50)
print(f'Valores na lista: {valores}')
maior = max(valores)
menor = min(valores)
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(pos, end=' ')
print()
print(f'O maior valor digitado foi {maior} na(s) posição(ões) ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(pos, end=' ')
print()
print('='*50)
