from flask import Blueprint
from app.blueprints.index_blueprint import index_blueprint

class AppBlueprints:

  def __init__(self, app):
    self.app = app

  def register_app_blueprints(self):
    self.app.register_blueprint(index_blueprint)
