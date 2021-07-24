"""
Crie um pacote chamado utilidades que tenha dois módulos internos chamados moeda e
dado. Transfira todas as funções utilizadas nos exercícios 107, 108 e 109 para o
primeiro pacote e mantenha tudo funcionando.
"""

from utilidades import moeda
from exercicios.geral import tratamento

p = tratamento.leiaFloat('Digite o preço: R$', 'preço')
moeda.resumo(p, 15, 23)
