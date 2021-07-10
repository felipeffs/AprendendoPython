# 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
# ex: Não importa o que os seus olhos veem, o que importa é o que o seu coração sente.
f = str(input('Digite uma frase:\n')).strip()

fqa = f.lower().count('a')
fqap = f.lower().find('a') + 1
fqau = f.lower().rfind('a') + 1

print("\nA letra 'a' parece {} vezes na frase e a primeira aparição é na {}ª posição e a ultima na {}ª posição".format(fqa, fqap, fqau))
