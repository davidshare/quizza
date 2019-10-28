from flask_cli import FlaskCLI
import unittest
import coverage

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

def run_coverage():
  cov = coverage.Coverage(
		branch=True,
		include='app/tests/*',
	)
  cov.start()
  tests = unittest.TestLoader().discover('app/tests', pattern='*test.py')
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

