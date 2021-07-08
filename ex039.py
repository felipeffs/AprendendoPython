import datetime
ano = int(input('Qual o seu ano de nascimento? '))
atual = datetime.date.today().year
idade = atual - ano

if idade == 18:
    print('Está na hora de se alistar no exército brasileiro')
elif idade < 18:
    print('falta {} ano(s) para se alistar'.format(18 - idade))
    print('Seu alistamento será em {}'.format(atual + (18 - idade)))
else:
    print('Já passou {} ano(s), se não se alistou se aliste imediatamente'.format(idade - 18))
    print('Deveria ter se alistado em {}'.format(atual + (18 - idade)))

# EXTRA: Adicionar o gênero e dizer se precisa se alistar obrigatoriamente