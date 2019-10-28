from os import environ, getenv
import unittest
from config.utils import get_env_vars

environ['TEST_VALUE'] = 'test_value'


class UtilsTest(unittest.TestCase):

  def test_can_get_environment_variables(self):
    self.assertFalse(get_env_vars('TEST_VALUE') is 'DAVID')
    self.assertEqual(get_env_vars('TEST_VALUE'), 'test_value')

  def return_None_if_environment_variable_does_not_exist(self):
    self.assertEqual(get_env_vars('TEST_VALUE2'), None)

if __name__ == '__main__':
  unittest.main()
