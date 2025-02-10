import requests 

# Parámetros
owner = 'IvanMendozaME'  # Ejemplo: 'octocat'
repo = 'upcreate'   # Ejemplo: 'Hello-World'
path = 'costumize.json' # Ejemplo: 'path/to/file.txt'
#token = 'tu-token-de-autenticacion'  # Necesitas un token de GitHub si el repositorio es privado

# URL de la API de GitHub
url = f'https://github.com//{owner}/{repo}/{path}'
                            
response = requests.get(url)

if response.status_code == 200:
    file_content = response.json()['content']
    print(file_content)
else:
    print(f'Error: {response.status_code} - {response.reason}')