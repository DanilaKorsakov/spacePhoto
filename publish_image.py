import os
import random
import argparse

import telegram
from dotenv import load_dotenv


def main():

    load_dotenv()
    
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    bot = telegram.Bot(token=telegram_bot_token)
    chat_id=os.getenv('TG_CHAT_ID')
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", help="Вставьте какую фотографию отправить на канал")
    args = parser.parse_args()
    
    if args.image == None:
        all_files = os.walk("images")
        for array_of_files in all_files:
            folder, nested_folder, files = array_of_files
            image = random.choice(files)
    else:
        image = args.image
    
    path = os.path.join('images', image)
    with open(path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


if __name__ == '__main__':
    main()