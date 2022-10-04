import os
import random
import argparse

import telegram
from dotenv import load_dotenv


def main():

        load_dotenv()

        telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

        bot = telegram.Bot(token=telegram_bot_token)
        chat_id=os.getenv('CHAT_ID')

        parser = argparse.ArgumentParser()
        parser.add_argument("--image", help="Вставьте какую фотографию отправить на канал")
        args = parser.parse_args()

        if args.image == None:
                all_files = os.walk("images")
                for array_of_files in all_files:
                        image = random.choice(array_of_files[2])
        else:
            image = args.image

        with open(f'images/{image}','rb') as file:
                photo = file
                bot.send_document(chat_id=chat_id, document=photo)


if __name__ == '__main__':
        main()