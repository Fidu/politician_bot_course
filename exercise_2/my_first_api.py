import logging

from flask import Flask
from config import HOST, PORT

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('my_first_api')

app = Flask('my_first_api')


@app.route('/')
def hello():
    return "My first API with Flask \n"


# TODO: Añadir decorador
def example_string(name):
    # TODO: Añadir comportamiento al recibir un string llamado name
    return result


# TODO: Añadir decorador
def example_integer(numeric):
    # TODO: Añadir comportamiento al recibir un entero llamado numerix
    return result


if __name__ == '__main__':
    logger.info(f'Levantando servidor en {HOST} en el puerto {PORT} ...')
    app.run(host=HOST, debug=True, port=PORT)
