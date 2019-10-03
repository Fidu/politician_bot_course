# Politician Bot Course
Repositorio del taller "Creando un deep-bot from scratch" con el que se pretende enseñar 
cómo crear un bot de Telegram (que utilice inteligencia artificial) desde 0. Para ello se
introducirán las herramientas y tecnologı́as necesarias para poder desplegar un modelo de 
Deep Learning y obtener los resultados de la red neuronal.

## Requisitos técnicos para asistir al taller
El taller se puede seguir a través de la imagen [Docker](https://www.docker.com/) creada 
a medida para el taller, o bien instalando lo necesario de forma manual.

### Preparación de entorno vía Docker
Si tienes instalado Docker simplemente **es necesario crear un directorio vacío** y ejecutar lo siguiente, cambiando 
**[USER_PATH]** por la ruta donde quieras que se clone el proyecto:

```bash
$ sudo docker run -i -t -p 5555:5555 -v [USER_PATH]:/root/politician_bot_course  edgarperezsampedro/politician_bot_course:latest
```

### Preparación del entorno de forma manual
Para preparar el entorno de forma manual es necesario hacer lo siguiente:

* Clonar el proyecto.
* Python 3.6.
* Instalación de librerias.

#### Clonar proyecto
Es necesario clonar el proyecto para obtener el código y los datos que usaremos durante el taller:

```bash
$ git clone https://github.com/Fidu/politician_bot_course
```

#### Instalación de librerías
En caso de no tener Docker, para la instalación manual de las librerías bastaría con ejecutar en la carpeta raiz del proyecto:

```bash
$ pip install -r requirements.txt
```

En caso de querer instalarlas una por una estan son las librerías y sus versiones que 
utilizaremos en el taller:

```text
flask==1.0.2
python-telegram-bot==11.1.0
requests==2.21.0
torch==1.1.0
```
