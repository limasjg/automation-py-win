import requests
from PIL import Image
from io import BytesIO
import os
from bs4 import BeautifulSoup

def get_image_url(page_url):
    """Obtém a URL da imagem a partir da página fornecida."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(page_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('meta', property='og:image')['content']
    return None

def download_image(image_url, base_filename='imagem_baixada', extension='.jpg'):
    """Baixa a imagem da URL fornecida e salva com um nome único."""
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            contador = 1
            filename = f'{base_filename}{extension}'
            while os.path.exists(filename):
                filename = f'{base_filename}{contador}{extension}'
                contador += 1
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f'O arquivo {filename} foi baixado com sucesso como um arquivo JPG.')
        else:
            print('Falha ao baixar a imagem.')
    except Exception as e:
        print(f'Ocorreu um erro ao baixar a imagem: {e}')

# URL da página que contém a imagem
url_da_pagina = 'https://unsplash.com/pt-br/fotografias/um-homem-parado-em-frente-a-algumas-pedras-ecw2GLQqVus'

# Obter a URL da imagem
url_da_imagem = get_image_url(url_da_pagina)

# Baixar a imagem
if url_da_imagem:
    download_image(url_da_imagem)
