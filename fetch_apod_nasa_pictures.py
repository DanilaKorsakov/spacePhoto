import random
import os

import requests
from save_image import save_image
from dotenv import load_dotenv
from urllib.parse import urlparse


def get_extension(url):
    try:
        path = urlparse(url).path
        return os.path.splitext(path)[1]
        return True
    except:
        return False


def main():

        load_dotenv()

        nasa_api_token = os.getenv('NASA_API_TOKEN')

        count = random.randint(30,50)

        payload = {
          "api_key": nasa_api_token,
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


if __name__ == '__main__':
        main()