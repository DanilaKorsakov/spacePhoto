import random
import os

import requests
from dotenv import load_dotenv
from save_image import save_image


def main():

    load_dotenv()

    nasa_api_token = os.getenv('NASA_API_TOKEN')

    payload = {
      "api_key": nasa_api_token
    }

    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()

    epic_random = random.randint(5, 10)

    for index in range(epic_random):
        file_name=f'epic_{index+1}.png'
        data = response.json()[index]
        date = data['date'].split()[0]
        date = date.split('-')
        name = data['image']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{name}.png'
        
        save_image(epic_image_url, file_name, payload)


if __name__ == '__main__':
    main()