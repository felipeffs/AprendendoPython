"""
Adicione ao módulo moeda.py criado nos exercícios anteriores, uma função chamada
resumo(), que mostre na tela algumas informações geradas pelas funções que já temos
no módulo criado até aqui.
"""

import moeda
from exercicios.geral import tratamento

p = tratamento.leiaFloat('Digite o preço: R$', 'preço')
moeda.resumo(p, 80, 35)
