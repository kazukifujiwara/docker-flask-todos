"""
This is a view module called by app.py
"""
from flask import Blueprint, render_template

view_bp = Blueprint('view', __name__, url_prefix='/view')

@view_bp.route('/', methods=['GET'])
def view():
    return render_template('view.html', \
        title='TODO Application', \
        message=''
    )

