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
        chat_id=os.getenv('CHAT_ID')

        parser = argparse.ArgumentParser()
        parser.add_argument("--time", help="Вставьте с какой переодичностью отпрвлять фотографии (в секундах)")
        args = parser.parse_args()
        periodicity = args.time

        while True:

                all_files = os.walk("images")

                for array_of_files in all_files:
                       random.shuffle(array_of_files[2])
                       for image in array_of_files[2]:
                               with open(f'images/{image}','rb') as file:
                                        photo = file
                                        bot.send_document(chat_id=chat_id, document=photo)
                               time.sleep(5)
                if periodicity == None:
                    periodicity = 4*60*60
                time.sleep(int(periodicity))


if __name__ == '__main__':
        main()