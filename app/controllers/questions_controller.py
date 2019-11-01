from app.helpers.controller_helper import ControllerHelper

class QuestionController(ControllerHelper):

  def __init__(self, request):
    ControllerHelper.__init__(self, request)

  def add_question(self):
    return self.request.get_json()

