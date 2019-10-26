import os
from flask import Flask
from app.utils.utils import get_env_vars

from .config import config


def create_app(config_override=None):
  '''
    function to create a flask application
    this utilizes the factory pattern

    :param config_override: Overide default configuration settings
    :returns app: Flask app
  '''

  app=Flask(__name__, instance_relative_config=True)
  default_config = os.getenv('FLASK_ENV', 'development')

  if config_override:
    app.config.from_object(config[config_override])
  else:
    app.config.from_object(config[default_config])

  return app
