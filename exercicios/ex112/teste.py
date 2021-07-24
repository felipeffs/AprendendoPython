"""
Dentro do pacote utilidades que criamos no exercício 111, temos um módulo chamado
dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a
função input(), mas com uma validação de dados para aceitar apenas valores que
sejam monetários.
"""

from utilidades import moeda
from utilidades import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 15, 23)
