"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e
idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma
nova pessoa e listar todas as pessoas cadastradas.
"""

from interface import *
from arquivo import *
from time import sleep
op = ('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')
arq = 'banco.txt'
# lista de funções
f = lerArquivo, cadastrar

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(op)
    sleep(0.3)
    if resp < len(op) and resp != 0:
        # Execução das funções de forma otimizada
        f[resp-1](arq)
    elif resp == len(op):
        titulo('Até logo!')
        break
    else:
        print('\033[31mERRO! Opção inexistente\033[m')
