lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita', 'Nachos'
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[1:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[:-2])
print(lanche)

# Tuplas são imutáveis
# prova: lanche[3] = 'Alface'

print('-'*50)
for comida in lanche:
    print(comida)
print('-'*50)
for comida in range(0, len(lanche)):
    print(lanche[comida])
print('-'*50)
for pos, comida in enumerate(lanche):
    print(comida, pos)
print('-'*50)
for pos in range(0, len(lanche)):
    print(lanche[pos], pos)
print('-'*50)

# Em ordem alfabética
print(sorted(lanche))

print('-'*50)

a = 2, 5, 4
b = 5, 8, 1, 2
print(a)
print(b)
print('-'*50)
c = a + b
print(c)
print('-'*50)
c = b + a
print(c)
print('-'*50)
print(c.count(5))
print('-'*50)
print(c.index(4))
print('-'*50)
print(c.index(5, 1))

print('-'*50)
# Uma única tupla em python aceita tipos diferentes
pessoa = ('Vinicius', 27, 'M', 75)
print(pessoa)

# Pode apagar uma tupla mas não um item especifico
# del(pessoa)