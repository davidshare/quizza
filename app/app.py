from app.utils.utils import get_env_vars
from app.main import create_app
from flask_cli import FlaskCLI
import unittest
import coverage

from dotenv import load_dotenv

load_dotenv()

app = create_app(get_env_vars('FLASK_ENV'))
FlaskCLI(app)

@app.cli.command("tests")
def run_tests():
  '''
  Run tests
  '''
  print('running tests -------------')
  tests = unittest.TestLoader().discover('app/', pattern='*test.py')
  results = unittest.TextTestRunner(verbosity=3).run(tests)
  if results.wasSuccessful():
    return 0
  return 1

@app.cli.command("coverage")
def run_coverage():
  cov = coverage.Coverage(
		branch=True,
		include='app/*',
		omit=['app/*test.py', 'app/app.py']
	)
  cov.start()
  tests = unittest.TestLoader().discover('app/', pattern='*test.py')
  results = unittest.TextTestRunner(verbosity=3).run(tests)
  if results.wasSuccessful():
    cov.stop()
    cov.save()
    print('************************************* SUMMARY OF COVERAGE *************************************')
    cov.report()
    cov.html_report(directory='coverage')
    cov.erase()
    return 0
  return 1


if __name__ == '__main__':
  app.run()
