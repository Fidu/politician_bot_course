import os
from setuptools import find_packages, setup
import src

readme = os.path.join(os.path.dirname(__file__), 'README.md')

with open(os.path.join(os.path.dirname(__file__),
                       'requirements.txt')) as requirements:
    install_requires = requirements.readlines()

setup(name='exercise 4',
      version=0.1,
      description="My first LSTM to generate text",
      long_description=open(readme).read(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: Other/Proprietary License',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Build Tools',
          ],
      keywords='AI, Machine Learning, RNN',
      author='Edgar Pérez Sampedro',
      author_email='edgar.perez.sampedro@gmail.com',
      url='https://github.com/Fidu/politician_bot_course',
      license='All rights reserved',
      packages=find_packages(),
      package_data={'': ['conf/*']},
      install_requires=install_requires,
      include_package_data=True,
      zip_safe=False
      )
