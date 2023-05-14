"""
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.
"""
# Extra: fazer km, hm, dam, m, dm, cm, mm.

valorM = float(input('Digite um valor em metros: '))

valorDm = valorM * 10
valorCm = valorDm * 10
valorMm = valorCm * 10
valorDam = valorM / 10
valorHm = valorDam / 10
valorKm = valorHm / 10

print('{} quilômetros | {} hectômetros | {} decâmetros | '.format(valorKm, valorHm, valorDam) +
      '\033[1m {} metros \033[0m | '.format(valorM) +
      '{} decímetros | {} centímetros | {} milímetros '.format(valorDm, valorCm, valorMm))
