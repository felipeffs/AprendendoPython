"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

valores = int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), \
          int(input('Digite o terceiro número: ')), int(input('E agora o quarto número: '))

print('='*50)
print(f'Você digitou os valores {valores}')
print(f"Quantidade de 9's: {valores.count(9)}")

if 3 not in valores:
    print("Nenhum valor 3 foi digitado")
else:
    print(f"Posição do primeiro valor 3: {valores.index(3) + 1}ª")
print(f'Valores pares digitados: ', end='')

par = False
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
        par = True
if not par:
    print('Nenhum')
