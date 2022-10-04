import requests

from pathlib import Path


def save_image(url,filename):

        full_name = 'images/{}'.format(filename)
        response = requests.get(url)
        response.raise_for_status()

        with open(full_name, 'wb') as file:
            file.write(response.content)

def main():

        Path("images").mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
        main()

  

