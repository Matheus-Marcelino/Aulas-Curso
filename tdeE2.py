from requests import get

url = "http://pudim.com.br/"

if get(url).status_code == 200:
    print("O servidor está disponível.")
else:
    print("O servidor está indisponível.")
