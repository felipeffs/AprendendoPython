"""
Adapte o código do exercício 107, criando uma função adicional chamada moeda() que
consiga mostrar os valores como um valor monetário formatado.
"""

import moeda
from exercicios.geral import tratamento

p = tratamento.leiaFloat('Digite o preço: R$', 'preço')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
