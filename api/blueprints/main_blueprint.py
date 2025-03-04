from flask import Blueprint


main_views = Blueprint("main", __name__)

@main_views.route('/character')
def get_character_name():
    character = "alsk;dj"
    return {'character': "123123123"}

