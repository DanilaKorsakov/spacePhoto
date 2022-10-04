import requests
import argparse

from save_image import save_image


def main():

        parser = argparse.ArgumentParser()
        parser.add_argument("--id", help="Вставьте id запуска spaceX")
        args = parser.parse_args()

        if args.id == None:
                id = '5eb87d42ffd86e000604b384'
        else:
                id = args.id

        url = 'https://api.spacexdata.com/v5/launches/{}'.format(id)
        response = requests.get(url)
        response.raise_for_status()

        pictures = response.json()['links']['flickr']['original']

        filename = 'spaceX_'

        for index,picture in enumerate(pictures):
            full_name = f'{filename}{index+1}.jpg'
            save_image(picture,full_name)


if __name__ == '__main__':
        main()