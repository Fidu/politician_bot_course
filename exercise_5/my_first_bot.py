import logging
import requests

from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_KEY, HOST, PORT

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('generate_text_bot')


def generate_text(bot, update, args):
    # TODO: coger parámetros de args (contexto y longitud a inferir)

    # TODO: Definir llamada_api para hacer la consulta a tu api y recibir la contraseña generada
    result_predict = requests.get(llamada_api).text

    logger.debug('Predicción -> ' + str(result_predict))
    bot.send_message(chat_id=update.message.chat_id, text=f'{result_predict}')


if __name__ == '__main__':
    updater = Updater(TELEGRAM_KEY)
    updater.dispatcher.add_handler(CommandHandler('sobre', generate_text, pass_args=True))

    logger.info('Ejecutando bot...')
    updater.start_polling()
    updater.idle()
