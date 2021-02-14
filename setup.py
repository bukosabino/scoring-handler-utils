from setuptools import setup

setup(name='scoringhandlerutils',
      version='0.0.2',
      description='Utils functions for scoring handler',
      url='https://github.com/bukosabino/scoring-handler-utils',
      author='Dario Lopez Padial (Bukosabino)',
      author_email='bukosabino@gmail.com',
      license='The MIT License (MIT)',
      packages=['api_model_utils'],
      install_requires=['scikit-learn', 'pyinstrument', 'yappi'],
      zip_safe=False
)
