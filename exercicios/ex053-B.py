"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
Ex: Após a sopa
    A sacada da casa
    A torre da derrota
    O lobo ama o bolo
    Anotaram a data da maratona
"""

f = str(input('Digite uma frase ')).lower().strip()
fs = f.split(' ')
junto = ''.join(fs)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('"{}" é um palíndromo'.format(f))
else:
    print('"{}" não é um palíndromo'.format(f))
