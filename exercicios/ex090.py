"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em
um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

while True:
    aluno = {'Nome': str(input(f"Nome: ")).strip().title()}
    if aluno['Nome'].isalpha():
        break
    print('\033[31mNome Inválido! Digite novamente.\033[m')
while True:
    aluno['Média'] = str(input(f'Média de {aluno["Nome"]}: ')).strip()
    mTemp = aluno['Média'].replace('.', '')
    if mTemp.isdigit():
        aluno['Média'] = float(aluno['Média'])
        break
    print('\033[31mValor Inválido! Digite novamente.\033[m')

print('—'*50)
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
