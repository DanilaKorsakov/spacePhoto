import requests
import os

from pathlib import Path

Path("images").mkdir(parents=True, exist_ok=True)


def save_image(url, filename, key=''):
  
    full_name = os.path.join('images', filename)
    
    response = requests.get(url, params=key)
      
    response.raise_for_status()
    
    with open(full_name, 'wb') as file:
        file.write(response.content)
