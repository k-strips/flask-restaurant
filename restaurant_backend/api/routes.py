from flask import current_app as app
from flask import Blueprint
from ..services.restaurant_service import create_restaurant

# blueprint configuration
api_bp = Blueprint("api", __name__)

@api_bp.route('/api/v1/restuarants', methods=['GET'])
def get_restuarants():
    return "hello world"