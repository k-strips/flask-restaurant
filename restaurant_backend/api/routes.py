from flask import current_app as app
from flask import Blueprint
from ..services.restaurant_service import create_restaurant, fetch_all_restaurants, get_restaurant_by_id, update_restaurant_by_id, update_restaurants, delete_restaurant_by_id, delete_restaurants

# blueprint configuration
api_bp = Blueprint("api", __name__)

@api_bp.route('/restuarants/add', methods=['POST'])
def add_restaurant(restaurant_data):
    return create_restaurant(restaurant_data)


@api_bp.route('/restuarants/update/<int:restuarant_id>', methods=['PUT'])
def update_restaurant_by_id(restaurant_data):
    return update_restaurant_by_id(restaurant_data)


@api_bp.route('/restuarants/update/', methods=['PUT'])
def update_restaurants(restaurants_data):
    return update_restaurants(restaurants_data)


@api_bp.route('/restuarants', methods=['GET'])
def fetch_all_restuarants():
    return fetch_all_restaurants()


@api_bp.route('/restuarants/<int:restuarant_id>', methods=['GET'])
def get_restaurant(restuarant_id):
    return get_restaurant_by_id(restuarant_id)


@api_bp.route('/restuarants/delete/<int:restuarant_id>', methods=['DELETE'])
def delete_restuarant_by_id(restuarant_id):
    return delete_restuarant_by_id(restuarant_id)


@api_bp.route('/restuarants/delete', methods=['DELETE'])
def delete_restaurants():
    return delete_restaurants()
