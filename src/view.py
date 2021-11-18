from flask import Blueprint, render_template
from flask import jsonify

view_bp = Blueprint('view', __name__, url_prefix='/view')

@view_bp.route('/', methods=['GET'])
def view():
    return render_template('view.html', \
        title='TODO App', \
        message='This is a sample TODO app.'
    )

