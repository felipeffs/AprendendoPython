"""
Faça um programa que leia uma frase pelo teclado e mostre:
▸ Quantas vezes aparece a letra "A".
▸ Em que posição ela aparece a primeira vez.
▸ Em que posição ela aparece a última vez.
"""

# frases: Não importa o que os seus olhos veem, o que importa é o que o seu coração sente.

f = str(input('Digite uma frase:\n')).lower().strip()

fQtdA = f.count('a')
fPrimeiroA = f.find('a') + 1
fUltimoA = f.rfind('a') + 1

print("\nA letra 'a' aparece {} vezes na frase e a primeira aparição é na {}ª posição "
      "e a ultima na {}ª posição".format(fQtdA, fPrimeiroA, fUltimoA))
