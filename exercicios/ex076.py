produtos = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Monitor IPS FHD', 699.99, 'RTX 3090', 15460.50

print('—'*54)
print(f'{"LISTAGEM DE PREÇO":^54}')
print('—'*54)
for p in range(0, len(produtos), 2):
    print(f'{produtos[p]:▪<43}R${produtos[p+1]:>9.2f}')
print('—'*54)
