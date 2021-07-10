cond = ' '
total = mProdutos = pBarato = 0
barato = ''
print('-'*53)
print(f'{"Atacadão Fogo Baixo":🔥^40}')
while cond not in 'N':
    print('-' * 53)
    produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    print('-'*53)
    cond = ' '
    while cond not in 'NS':
        cond = str(input('Tem mais produtos? ')).strip().upper()[0]
    total += preco
    if preco > 1000:
        mProdutos += 1
    if pBarato == 0 or pBarato > preco:
        barato = produto
        pBarato = preco
print('-' * 53)
print('>>Infos:\n'
      f'\n-Valor total da compra: {total:.2f}'
      f'\n-Quantidade de produtos acima de R$1000.00: {mProdutos}'
      f'\n-Produto mais barato: {barato} por R${pBarato}')
