import logging
import requests

from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_KEY, HOST, PORT

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('generate_text_bot')


def generate_text(bot, update, args):
    try:
        params = str(args[0]).replace('_', ' ') + '/' + str(args[1])
    except IndexError:
        logger.warning('No hay longitud de predicción devolviendo logitud por defecto...')
        params = str(args[0]).replace('_', ' ')

    url = 'http://' + HOST + ':' + str(PORT)
    result_predict = requests.get(url + '/predict/' + params).text

    logger.debug('Predicción -> ' + str(result_predict))
    bot.send_message(chat_id=update.message.chat_id, text=f'{result_predict}')


if __name__ == '__main__':
    updater = Updater(TELEGRAM_KEY)
    updater.dispatcher.add_handler(CommandHandler('sobre', generate_text, pass_args=True))

    logger.info('Ejecutando bot...')
    updater.start_polling()
    updater.idle()
