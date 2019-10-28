import os
from .utils import get_env_vars

class Config:
  '''
    class with base configuration for the app
  '''
  SECRET_KEY = get_env_vars('SECRET_KEY')
  DEBUG = False

class ProductionConfig(Config):
  '''
    class with configuration for the production environment
  '''
  DB_URL = get_env_vars('PROD_DB_URL')

class DevelopmentConfig(Config):
  '''
    class with configuration for the development environment
  '''
  DEBUG=True
  DB_URL = get_env_vars('DEV_DB_URL')

class TestConfig(Config):
  '''
    class with configuration for the test environment
  '''
  DB_URL = get_env_vars('TEST_DB_URL')

config = {
    'development': DevelopmentConfig,
    'staging': ProductionConfig,
    'production': ProductionConfig,
    'testing': TestConfig
}
