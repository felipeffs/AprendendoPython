def contador(inicio, fim, passo):
    from time import sleep
    print('-'*50)
    if fim < inicio:
        if passo > 0:
            passo *= -1
        elif passo == 0:
            passo = -1
        print(f'Contagem de {inicio} até {fim} de {passo * -1} em {passo * -1}')
        fim -= 1
    else:
        if passo < 0:
            passo *= -1
        elif passo == 0:
            passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        fim += 1
    for i in range(inicio, fim, passo):
        sleep(0.3)
        print(f'{i} ', end='')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-'*50)
print('Agora é você! Isso mesmo! Você vai customizar a próxima contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
print('-'*50)
