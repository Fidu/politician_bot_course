import logging
import json

from flask import Flask
from GeneratorTextLSTM import load_model, sample
from config import HOST, PORT, PATH_MODEL, PATH_DATA

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('lstm_generator_server')

app = Flask('lstm_generator_server')


@app.route('/predict/<init_context>', methods=['GET'])
@app.route('/predict/<init_context>/<int:len_result>', methods=['GET'])
def predict(init_context, len_result=1000):
    predict_result = sample(model, len_result, prime=init_context, top_k=5)
    logger.debug(predict_result)

    return predict_result


if __name__ == '__main__':
    logger.debug('Preparando datos y modelo...')
    with open(PATH_DATA, 'r') as js_input:
        data_input = json.load(js_input)
    logger.debug('Datos cargados -> ' + str(data_input))

    global model
    model = load_model(data_input, PATH_MODEL)

    logger.info(f'Levantando servidor en {HOST} en el puerto {PORT} ...')
    app.run(host=HOST, debug=True, port=PORT)
