from flask import Flask
from blueprints.main_blueprint import main_views
import time

app = Flask(__name__) 

app.register_blueprint(main_views)


