def escreva(texto):
    tam = len(texto) + 4
    print('~'*tam)
    print('  ' + texto.title().strip() + '  ')
    print('~'*tam)


escreva(str(input('Digite uma frase: ')))
