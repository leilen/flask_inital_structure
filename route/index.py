from flask import Blueprint,render_template

blueprint = Blueprint('route',__name__)

@blueprint.route('/')
def route():
    return render_template('/index.html')