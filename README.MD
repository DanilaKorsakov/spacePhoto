# Космический телеграм

Данный проект скачивает фотографии с запуска SpaceX.
Также программа скачивает фотографии из косомса от NASA, а также фотографии земли.
После скачиваня можно опубликовать данные фотографии в телеграм канале.

## Как установить

Для запуска программы необходимо установить Python от 3 версии.
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:  

```
pip install -r requirements.txt
``` 

Для запуска скрипта с телеграм ботом небодимо его создать. Для этого необходимо обратиться к [Отцу Ботов](https://telegram.me/BotFather)
В дилоге необходимо запустить две команды : `/start` `/newbot`. Далее следуем его инструкциям.

Как создать канал в телеграме можно найти [здесь](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)

Перед запуском программы не забудьте склонировать проект или скачать его архив
В папке с проектом необходимо создать .env файл, где вы укажете ваш токен API NASA, токен телеграм бота и id канала в телеграме

```
NASA_API_TOKEN=Ваш токен с API NASA
TELEGRAM_BOT_TOKEN=Ваш токен телеграм бота
CHAT_ID=Ваша ссылка на канал
```

[Для получения токена API NASA](https://api.nasa.gov) 
 

## Как запустить

### Получаем фотографии с запусков spaceX

Чтобы скачать фотографии с последнего запуска spaceX необходимо просто запустить программу:

```
python fetch_spacex_images.py 
``` 

Для получения фотографий с определенного запуска немобходимо указать его id:

```
python fetch_spacex_images.py --id ID
``` 

### Получаем фотографии космоса от NASA

Для получения фотографий космоса необходимо запустить программу:

```
python fetch_apod_nasa_pictures.py
``` 

### Получаем фотографии земли

Для получения фотографий земли необходимо запустить программу:

```
python fetch_epic_nasa_pictures.py
``` 

### Публикуем все фотогорафии в телеграм канал

Для публикации полученных фотографий из папки images запустите скрипт:

```
python publisher_bot.py
``` 

Чтобы указать с какой переодичностью публиковать файлы в телеграм канал укажите аргумент --time:

```
python publisher_bot.py --time Время в секундах
``` 

### Публикуем конкретную фотографию в телеграм канал

Для публикации конкретной фотографии необходимо запустить программу со следующими аргументами:

```
python publish_image.py  --image название фотографии
``` 

Если опустить аргумент `--image` то отправляется случайная фотография из папки images

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
