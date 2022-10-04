import os
import requests
import random

from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

NASA_API_TOKEN = os.getenv('NASA_API_TOKEN')

def save_image(url,filename):
  
    full_name = 'images/{}'.format(filename)
    response = requests.get(url)
    response.raise_for_status()

    with open(full_name, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch():
  
    id = '5eb87d42ffd86e000604b384'
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(id)
    response = requests.get(url)
    response.raise_for_status()
    
    pictures = response.json()['links']['flickr']['original']
    
    filename = 'spaceX_'
    
    for index,picture in enumerate(pictures): 
        full_name = f'{filename}{index+1}.jpg'
        save_image(picture,full_name)

def get_extension(url):
    try:
        path = urlparse(url).path
        return os.path.splitext(path)[1]
        return True
    except:
        return False
def fetch_nasa_pictures(token):

    count = random.randint(30,50)

    payload = {
      "api_key": token,
      "count": count
    }
    
    url = 'https://api.nasa.gov/planetary/apod'
    
    response = requests.get(url, params=payload)
    response.raise_for_status()

    filename = 'NASA_'
    
    for index, api_response in enumerate(response.json()):
        link = api_response['url']
        extension = get_extension(link)
        if(extension):
            full_name = f'{filename}{index+1}{extension}'
            save_image(link, full_name)


def fetch_epic(token):
    payload = {
      "api_key": token
    }
    
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()

    epic_random = random.randint(5,10)
  
    for index in range(epic_random):
        file_name=f'epic_{index+1}.png'
        data = response.json()[index]
        date = data['date'].split()[0]
        date = date.split('-')
        name = data['image']
        epic_iamge_url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{name}.png?api_key={token}'  
        save_image(epic_iamge_url,file_name)


Path("images").mkdir(parents=True, exist_ok=True)


fetch_spacex_last_launch()
fetch_nasa_pictures(NASA_API_TOKEN)
fetch_epic(NASA_API_TOKEN)


  

