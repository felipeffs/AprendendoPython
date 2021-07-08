nt1 = float(input('Digite a nota da primeira avaliação: '))
nt2 = float(input('Digite a nota da segunda avaliação: '))

media = (nt1 + nt2) / 2
print('A média do aluno é \033[32m{:.2f}\033[m'.format(media))
if media < 5:
    print('Está \033[31mREPROVADO!\033[m')
elif 5 <= media < 7:
    print('Está de \033[33mRECUPERAÇÃO\033[m')
else:
    print('Está \033[34mAPROVADO\033[m')
