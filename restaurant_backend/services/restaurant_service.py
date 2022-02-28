from ..models import Restaurant

def create_restaurant(restaurant_data):
    try:
        return "restuarant created"
    except Exception as e:
        return f'sorry, restuarant creation failed'


def update_restaurant(restaurant_id):
    try:
        return "restuarant updated"
    except Exception as e:
        return f'sorry, restuarant creation failed'


def list_all_restaurants():
    try:
        return "all restuarants ready"
    except Exception as e:
        return f'sorry, all restuarants failed'


def get_one_restaurant(restaurant_id):
    try:
        return "restuarant created"
    except Exception as e:
        return f'sorry, restuarant creation failed'


def delete_all_restaurants():
    try:
        return "all restuarants deleted"
    except Exception as e:
        return f'sorry, restuarant creation failed'


def delete_one_restaurant(restaurant_id):
    try:
        return "restuarant deleted"
    except Exception as e:
        return f'sorry, restuarant creation failed'