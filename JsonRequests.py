import requests 
import base64
import json

# Parámetros
owner = 'IvanMendozaME'  # Ejemplo: 'octocat'
repo = 'upcreate'   # Ejemplo: 'Hello-World'
path = 'costumize.json' # Ejemplo: 'path/to/file.txt'
#token = 'tu-token-de-autenticacion'  # Necesitas un token de GitHub si el repositorio es privado

# URL de la API de GitHub
url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
                            
response = requests.get(url)

if response.status_code == 200:
    try:
        response_json = response.json()
        #print(response_json)  # <-- Añadido para ver el contenido del JSON
        # El contenido del archivo está codificado en base64
        if 'content' in response_json:
            file_content_encoded = response_json['content']
            # Decodificar el contenido de base64 a una cadena JSON
            file_content_str = base64.b64decode(file_content_encoded).decode('utf-8')
            # Convertir la cadena JSON a un diccionario de Python
            contenido = json.loads(file_content_str)
            # Ahora puedes manipular el JSON como un diccionario
            print(contenido)
            print(contenido['Costumize'])
            

        else:
            print("El campo 'content' no se encontró en la respuesta JSON.")
    except requests.exceptions.JSONDecodeError:
        print("Error: la respuesta no es un JSON válido.")
else:
    print(f'Error: {response.status_code} - {response.reason}')