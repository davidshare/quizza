import unittest
from flask import current_app
from app.main_app import create_app
from config.utils import get_env_vars



class ConfigTest(unittest.TestCase):

  def test_development_environment(self):
    app = create_app('development')
    self.assertFalse(app.config['SECRET_KEY'] is 'DAVID')
    self.assertTrue(app.config['DEBUG'] is True)
    self.assertFalse(current_app is None)
    self.assertEqual(app.config['DB_URL'], get_env_vars('DB_URL'))
    self.assertEqual(app.config['DB_NAME'], get_env_vars('DEV_DB'))

class TestProductionConfig(unittest.TestCase):

  def test_production_environment(self):
    app = create_app('production')
    self.assertFalse(app.config['SECRET_KEY'] is 'DAVID')
    self.assertTrue(app.config['DEBUG'] is False)
    self.assertFalse(current_app is None)
    self.assertEqual(app.config['DB_URL'], get_env_vars('DB_URL'))
    self.assertEqual(app.config['DB_NAME'], get_env_vars('PROD_DB'))


class TestTestingConfig(unittest.TestCase):

  def test_testing_environment(self):
    app = create_app('testing')
    self.assertFalse(app.config['SECRET_KEY'] is 'DAVID')
    self.assertTrue(app.config['DEBUG'] is False)
    self.assertFalse(current_app is None)
    self.assertEqual(app.config['DB_URL'], get_env_vars('DB_URL'))
    self.assertEqual(app.config['DB_NAME'], get_env_vars('TEST_DB'))

if __name__ == '__main__':
  unittest.main()
