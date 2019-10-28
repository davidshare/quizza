from pymongo import MongoClient
from config.utils import get_env_vars

class AppDatabase:

  def __init__(self, app):
    self.app = app

  def db_connect(self):
    db_url = self.app.config['DB_URL']
    db_name = self.app.config['DB_NAME']
    client = MongoClient(db_url)
    db = client["{db_name}"]
    return db
