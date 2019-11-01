from pymongo import MongoClient
from config.utils import get_env_vars

class AppDatabase:

  def __init__(self, app):
    self.app = app
    db_url = app.config['DB_URL']
    db_name = app.config['DB_NAME']
    client = MongoClient(db_url)
    self.db = client["{db_name}"]
