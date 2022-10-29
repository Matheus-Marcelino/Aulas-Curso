from requests import get

url = 'http://pudim.com.br/'

if get(url).status_code == 200:
    print("O servidor está disponível.")
else:
    print("O servidor está indisponível.")


"""
-> maneira do professor

import urllib.request as urgit 

try:
    site = ur.urlopen('http://pudim.com.br/')
except:
    print('Deu Erro')
else:
    print('tudo ok')
"""
