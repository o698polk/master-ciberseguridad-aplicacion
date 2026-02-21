import requests

url = 'http://localhost:8080'

response = requests.get(url)

print(response.json())


def request_sumar(numero1, numero2):
    url = f'{url}/api/sumar'
    data = {
        'numero1': numero1,
        'numero2': numero2
    }
    response = requests.post(url, json=data)
    return response.json()