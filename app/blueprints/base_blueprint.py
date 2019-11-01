from flask import Blueprint, request
from app.blueprints.index_blueprint import index_blueprint
from app.blueprints.questions_blueprints import questions_blueprint

class AppBlueprints:
  def __init__(self, app):
    self.app = app

  def register_app_blueprints(self):
    self.app.register_blueprint(index_blueprint)
    self.app.register_blueprint(questions_blueprint)
