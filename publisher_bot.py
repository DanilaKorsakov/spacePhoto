import os
import random
import time
import argparse

import telegram
from dotenv import load_dotenv


def main():

    load_dotenv()

    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    bot = telegram.Bot(token=telegram_bot_token)
    chat_id = os.getenv('TG_CHAT_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument("--time", help="Вставьте с какой переодичностью отпрвлять фотографии (в секундах)", default='14400')
    args = parser.parse_args()
    periodicity = int(args.time)

    while True:

        all_files = os.walk("images")

        for array_of_files in all_files:
            folder, nested_folder, files = array_of_files
            random.shuffle(files)
            for image in files:
                path = os.path.join('images', image)
                with open(path, 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(5)
        time.sleep(periodicity)


if __name__ == '__main__':
    main()