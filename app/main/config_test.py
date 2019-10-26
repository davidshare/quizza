import unittest
from flask import current_app
from app.app import app
from app.main import create_app
from app.utils.utils import get_env_vars

class ConfigTest(unittest.TestCase):

  def test_development_environment(self):
    self.assertFalse(app.config['SECRET_KEY'] is 'DAVID')
    self.assertTrue(app.config['DEBUG'] is True)
    self.assertFalse(current_app is None)
    self.assertEqual(app.config['DB_URL'], get_env_vars('DEV_DB_URL'))

class TestProductionConfig(unittest.TestCase):

  def test_production_environment(self):
    app = create_app('production')
    self.assertFalse(app.config['SECRET_KEY'] is 'DAVID')
    self.assertTrue(app.config['DEBUG'] is False)
    self.assertFalse(current_app is None)
    self.assertEqual(app.config['DB_URL'], get_env_vars('PROD_DB_URL'))

class TestTestingConfig(unittest.TestCase):

  def test_testing_environment(self):
    app = create_app('testing')
    self.assertFalse(app.config['SECRET_KEY'] is 'DAVID')
    self.assertTrue(app.config['DEBUG'] is False)
    self.assertFalse(current_app is None)
    self.assertEqual(app.config['DB_URL'], get_env_vars('TEST_DB_URL'))

if __name__ == '__main__':
  unittest.main()
