import urllib.request
# w = webbrowser.open('www.pudim.com.br')
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'O site pudim está offline')
else:
    print('O site pudim está online')
    print(site.read())
