# Ejercicio 5
Este ya es el último ejercicio, en el cual utilizaremos lo aprendido en el curso para crear un bot que se comunique con nuestra API que a su vez se comunicará con nuestro *modelo* que hemos entrenado durante el taller e inferir un texto de la longitud que le indiquemos.

## Enunciado
Modificar y completar el código de **my_first_bot.py**, **my_first_api.py** y **lstm_generator.py**:

1. Configurar nuestro **config.py** añadiendo la ruta de nuestro modelo entrenado en el ejercicio anterior y crear el método *predict* dentro de **lstm_generator.py**.
2. Crear método en **my_first_api.py** que reciba un texto de contexto y un entero de longitud del texto y llame a la función predict de **lstm_generator.py**.
3. Crear un bot que tenga de entrada "/sobre crisis_económica 300" y llame a nuestra api y devuelva al usuario el resultado de la llamada del método creado en el punto 2.