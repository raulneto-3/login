import requests

# URL base da API
BASE_URL = 'http://127.0.0.1:5000/api'

# Credenciais de login
login_data = {
    'email': 'moriarty@king.com',
    'password': 'king'
}

# Função para testar o login e obter o token
def test_login():
    response = requests.post(f'{BASE_URL}/login', json=login_data)
    if response.status_code == 200:
        print('Login bem-sucedido!')
        token = response.json().get('access_token')
        print(f'Token: {token}')
        return token
    else:
        print('Falha no login:', response.json().get('msg'))
        return None

# Função para testar a rota protegida
def test_protected_route(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f'{BASE_URL}/protected', headers=headers)
    if response.status_code == 200:
        print('Acesso à rota protegida bem-sucedido:', response.json())
    else:
        print('Falha ao acessar a rota protegida:', response.json().get('msg'))

if __name__ == '__main__':
    token = test_login()
    if token:
        test_protected_route(token)