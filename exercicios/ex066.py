c = soma = 0

while True:
    n = int(input('Digite um número \033[0:31m(999 para parar)\033[m: '))
    if n == 999:
        break
    c += 1
    soma += n

if c == 0:
    print(f'\n\033[1:31mNenhum número foi informado\033[m')
elif c == 1:
    print(f'\n\033[1:32mO número informado foi {soma}\033[m')
else:
    print(f'\n\033[1:32mA soma dos {c} números informados foi {soma}\033[m')
