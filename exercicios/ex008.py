"""
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.
"""
# → Extra: fazer Km, hm, dam, m, dm, cm, mm.

valorM = float(input('Digite um valor em metros: '))
valorCm = valorM * 100
valorMm = valorCm * 10
print('{} metros é igual a {:.0f} centímetros, {:.0f} milímetros'.format(valorM, valorCm, valorMm))
