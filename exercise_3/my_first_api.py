import logging
import string

from flask import Flask
from random import choice
from config import HOST, PORT

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('secure_pass_generator')

app = Flask('secure_pass_generator')


@app.route('/secure_pass/<int:len_pass>', methods=['GET'])
def secure_pass(len_pass):
    base_chars = string.ascii_letters + string.punctuation + string.digits
    random_string = ''.join(choice(base_chars) for i in range(len_pass))

    logger.info(f'Contraseña generada -> {random_string}')
    return random_string


if __name__ == '__main__':
    logger.info(f'Levantando servidor en {HOST} en el puerto {PORT} ...')
    app.run(host=HOST, debug=True, port=PORT)
