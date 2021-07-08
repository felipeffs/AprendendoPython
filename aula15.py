c = 0
while True:
    c += 1
    print('\033[:35m {} \033[m'.format(c))
    if c == 1000:
        break
# nova formatação de string
print(f'Alou {c}')

numerofloat = 333.53

print(f'Olha que loco {numerofloat:.2f}')
