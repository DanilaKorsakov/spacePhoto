import requests
import argparse

from save_image import save_image


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="Вставьте id запуска spaceX", default='5eb87d42ffd86e000604b384')
    args = parser.parse_args()
    launch_id = args.id
    
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(launch_id)
    response = requests.get(url)
    response.raise_for_status()
    
    pictures = response.json()['links']['flickr']['original']
    
    filename = 'spaceX_'
    
    for index, picture in enumerate(pictures, start=1):
        full_name = f'{filename}{index}.jpg'
        save_image(picture, full_name)


if __name__ == '__main__':
    main()