from app.blueprints.base_blueprint import Blueprint
from app.controllers.index_controller import IndexController

index_blueprint = Blueprint('index', __name__, url_prefix='/api/v1')
index_controller = IndexController()

@index_blueprint.route('/', methods=['GET'])
def home_blueprint():
  return index_controller.index()
