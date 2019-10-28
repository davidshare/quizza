import os
from flask import Flask
from flask_cli import FlaskCLI

from config.utils import get_env_vars

from config.environment_config import config
from app.cli_commands import run_coverage, run_tests

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


app = create_app(get_env_vars('FLASK_ENV'))

FlaskCLI(app)

@app.cli.command("tests")
def tests():
  return run_tests()

@app.cli.command("coverage")
def coverage():
  return run_coverage()
