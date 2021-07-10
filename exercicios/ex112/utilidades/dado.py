def leiaDinheiro(msg=''):
    while True:
        numero = str(input(msg)).strip().replace(',', '.')
        n2 = numero.replace('.', '')
        if n2.isdigit():
            break
        print(f'\033[31m[!] - Preço inválido! Digite novamente.\033[m')
    return float(numero)
