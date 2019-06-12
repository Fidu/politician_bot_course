import logging

from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_KEY

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('my_first_bot')


def hello_someone(bot, update, args):
    # TODO: coger parámetro de args y enviarlo al usuario

    bot.send_message(chat_id=update.message.chat_id, text=texto_resultado)


if __name__ == '__main__':
    updater = Updater(TELEGRAM_KEY)
    updater.dispatcher.add_handler(CommandHandler('saludar', hello_someone, pass_args=True))

    logger.info('Ejecutando bot...')
    updater.start_polling()
    updater.idle()
