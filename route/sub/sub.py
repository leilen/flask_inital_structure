from flask import Blueprint,render_template

blueprint = Blueprint('sub',__name__)

@blueprint.route('/')
def route():
    return render_template('/sub/sub.html',name='name',count=100)