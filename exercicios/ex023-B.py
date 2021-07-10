"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados.
Ex:
Digite um número: 1834
unidade:4 dezena:3 centena:8 milhar:1
"""

n = int(input('Digite um número entre 0 a 9999: '))

u = n // 1 % 10
c = n // 10 % 10
d = n // 100 % 10
m = n // 1000 % 10

print("""\nMétodo Matemático:
>Unidade: {}
>Dezena: {}
>Centena: {}
>Milhar: {}
""".format(u, c, d, m))
