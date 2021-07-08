# 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nc = str(input('Nome completo: ')).strip()
nc = nc.split()
ultnomepos = len(nc) - 1

print('Primeiro nome: {} \nUltimo nome: {}'.format(nc[0], nc[ultnomepos]))
