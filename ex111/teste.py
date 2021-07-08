from utilidades import moeda
from geral import tratamento

p = tratamento.leiaFloat('Digite o preço: R$', 'preço')
moeda.resumo(p, 15, 23)
