alunos = list()
total = q = 0
while True:
    while True:
        quant = str(input('Quer adicionar quantos alunos? ')).strip()
        if quant.isdigit():
            quant = int(quant)
            break
        else:
            print('\033[31mQuantidade Inválida! Tente novamente.\033[m')
    if quant == 0:
        break
    total += quant
    for q in range(q, total):
        alunos.append(list())
        print('—'*100)
        alunos[q].append(str(input('Nome: ')).strip().title())
        alunos[q].append(list())
        for n in range(0, 2):
            alunos[q][1].append(float(input(f'Nota {n + 1}: ')))
        alunos[q].append(float((alunos[q][1][0] + alunos[q][1][1]) / 2))
        print('—' * 100)
    q += 1
print('—='*50)
print('\033[4m\033[1m', f'|{"No.":<4}', f'|{"Aluno":<30}', f'|{"Média":<5}|', '\033[m')
for pos, al in enumerate(alunos):
    print('\033[4m', f'|{pos:<4}', f'|{al[0]:<30}', f'|{al[2]:<5.2f}|', '\033[m')

while True:
    print('—=' * 50)
    while True:
        resp = str(input('Quer mostrar a nota de qual aluno? (999 interrompe) ')).strip()
        if resp.isdigit():
            resp = int(resp)
            if resp < len(alunos) or resp == 999:
                break
            else:
                print('\033[31mEsse valor não corresponde a nenhum aluno! Tente novamente.\033[m')
        else:
            print(f'\033[31mA numeração dos alunos é um número inteiro! Tente novamente.\033[m')
    if resp == 999:
        break
    print('—'*100)
    print(f'{alunos[resp][0]} tirou {alunos[resp][1][0]} na primeira e {alunos[resp][1][1]} na segunda avaliação')
    print('—'*100)
