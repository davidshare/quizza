from flask import Blueprint
from app.views import IndexController

index_blueprint = Blueprint('index', __name__, url_prefix='/api/v1')

@index_blueprint.route('/', methods=['GET'])
def home_blueprint():
  index_controller = IndexController()
  return index_controller.index()
