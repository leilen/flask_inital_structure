from flask import Flask , send_from_directory, render_template
from .sub import sub
from config import config

def create_app(mode):
    app = Flask(__name__,static_url_path='/static',template_folder='../templates',static_folder='../static')
    app.config.from_object(config[mode])

    app.register_blueprint(sub.blueprint,url_prefix='/sub')

    @app.route('/')
    def route():
        return render_template('index.html')

    return app