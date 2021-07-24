"""
Crie um código em Python que teste se o site Pudim está acessível pelo computador
usado.
"""

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'O site pudim está offline')
else:
    print('O site pudim está online')
    print(site.read())
