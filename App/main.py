#region IMPORTS
from flask import Flask
from App.views import views
#endregion

def add_views(app):
    for view in views:
        app.register_blueprint(view)    

def create_app(config_overrides={}):

    app = Flask(__name__, static_url_path='/static')
    
    add_views(app)
    return app