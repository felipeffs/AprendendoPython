from math import trunc

n = int(input('Digite um número entre 0 a 9999: '))

u = n // 1 % 10
c = n // 10 % 10
d = n // 100 % 10
m = n // 1000 % 10

print("""\nMétodo matematico:
>Unidade: {}
>Dezena: {}
>Centena: {}
>Milhar: {}
""".format(u, c, d, m))
