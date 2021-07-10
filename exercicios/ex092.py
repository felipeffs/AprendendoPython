# Considere 35 anos de contribuição para se aposentar
from datetime import datetime
info = dict()
info['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
info['carteira de trabalho'] = int(input('Carteira de Trabalho (0 - Não possui): '))
info['idade'] = datetime.now().year - nascimento
if info['carteira de trabalho'] != 0:
    info['contratação'] = int(input('Ano de Contratação: '))
    info['salario'] = float(input('Salário: R$'))
    info['aposentadoria'] = 35 - (datetime.now().year - info['contratação']) + info['idade']
print('='*50)
for k, v in info.items():
    print(f'{str(k).title()}: {v}')
