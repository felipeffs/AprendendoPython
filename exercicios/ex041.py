from datetime import date

ano = int(input('Ano de Nascimento do Atleta: '))

idade = date.today().year - ano

cat = 'master'
if idade <= 9:
    cat = 'mirim'
elif idade <= 14:
    cat = 'infantil'
elif idade <= 19:
    cat = 'junior'
elif idade <= 20:
    cat = 'sênior'

print('O atleta tem {} anos\nClassificação {}'.format(idade, cat.upper()))
