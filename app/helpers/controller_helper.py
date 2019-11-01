from flask import current_app
from app.helpers.database_helper import AppDatabase

class ControllerHelper:

  def __init__(self, request):
    self.request = request

  def request_data(self):
    return self.request.get_json()
