import logging

from flask import Flask
from config import HOST, PORT

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('my_first_api')

app = Flask('my_first_api')


@app.route('/')
def hello():
    return "My first API with Flask \n"


@app.route('/string/<name>', methods=['GET'])
def example_string(name):
    result = f'Hola {name}!'
    return result


@app.route('/integer/<int:numeric>', methods=['GET'])
def example_integer(numeric):
    result = f'Esto es un entero -> {numeric}'
    return result


if __name__ == '__main__':
    logger.info(f'Levantando servidor en {HOST} en el puerto {PORT} ...')
    app.run(host=HOST, debug=True, port=PORT)
