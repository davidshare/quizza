from utils.utils import get_env_vars
from main import create_app

app = create_app(get_env_vars('FLASK_ENV'))

if __name__ == '__main__':
  app.run()
