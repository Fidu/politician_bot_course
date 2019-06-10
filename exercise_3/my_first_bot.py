import logging
import requests

from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_KEY, HOST, PORT

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('secure_pass_bot')


def generate_pass(bot, update, args):
    try:
        len_pass = int(args[0])
    except (IndexError, ValueError):
        logger.warning('No hay parámetro de longitud o el parámetro no es un entero devolviendo valor por defecto...')
        len_pass = 8

    url = 'http://' + HOST + ':' + str(PORT)

    secure_pass = requests.get(url + '/secure_pass/' + str(len_pass)).text
    logger.info('Devolviendo resultado -> ' + f'Contraseña generada: {secure_pass}')
    bot.send_message(chat_id=update.message.chat_id, text=f'Contraseña generada: {secure_pass}')


if __name__ == '__main__':
    updater = Updater(TELEGRAM_KEY)
    updater.dispatcher.add_handler(CommandHandler('pass', generate_pass, pass_args=True))

    logger.info('Ejecutando bot...')
    updater.start_polling()
    updater.idle()
