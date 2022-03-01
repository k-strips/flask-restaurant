from ..models import Restaurant

def create_restaurant(restaurant_data):
    try:
        return f"restuarant created"
    except Exception as e:
        return f'sorry, restuarant creation failed'


def update_restaurant_by_id(restaurant_id):
    try:
        return f"restuarant with id {restaurant_id} updated"
    except Exception as e:
        return f'sorry, restuarant creation failed'


def update_restaurants(restaurants_data):
    try:
        return f"restuarants updated"
    except Exception as e:
        return f'sorry, restuarants update failed'


def fetch_all_restaurants():
    try:
        return "all restuarants ready"
    except Exception as e:
        return f'sorry, all restuarants failed'


def get_restaurant_by_id(restaurant_id):
    try:
        return f"restuarant with id {restaurant_id} ready"
    except Exception as e:
        return f'sorry, restuarant creation failed'


def delete_restaurants():
    try:
        return "all restuarants deleted"
    except Exception as e:
        return f'sorry, restuarant creation failed'


def delete_restaurant_by_id(restaurant_id):
    try:
        return f"restuarant with id {restaurant_id} deleted"
    except Exception as e:
        return f'sorry, restuarant creation failed'