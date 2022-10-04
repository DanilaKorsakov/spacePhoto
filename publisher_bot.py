import telegram


bot = telegram.Bot(token='5747439259:AAHnp_FCXv0SodG1UboqqjuI0MgUwALpUQ8')

chat_id='@image_pusblish'

bot.send_document(chat_id=chat_id, document=open('images/epic_1.png', 'rb'))