from app.blueprints.base_blueprint import Blueprint, request
from app.controllers.questions_controller import QuestionController


questions_blueprint = Blueprint('questions', __name__, url_prefix='/api/v1')
questions_controller = QuestionController(request)

@questions_blueprint.route('/questions', methods=['POST'])
def add_question_blueprint():
  return questions_controller.add_question()
