import logging
import json

from flask import Flask
from GeneratorTextLSTM import load_model, sample
from config import HOST, PORT, PATH_MODEL, PATH_DATA

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('lstm_generator_server')

app = Flask('lstm_generator_server')


# TODO: Añadir decorador
def predict(init_context, len_result):
    # TODO: Llamar al método sample (incluido en el fichero GeneratorTextLSTM.py) y guardarlo en predict_result

    logger.debug(predict_result)
    return predict_result


if __name__ == '__main__':
    logger.debug('Preparando datos y modelo...')
    # TODO: Añadir código para cargar un json en la variable data_input (json.load)
    logger.debug('Datos cargados -> ' + str(data_input))

    global model
    # TODO: Cargar modelo (llamar al método load_model del fichero GeneratorTextLSTM.py) y guardalor en model

    logger.info(f'Levantando servidor en {HOST} en el puerto {PORT} ...')
    app.run(host=HOST, debug=True, port=PORT)
