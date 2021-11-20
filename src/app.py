# from flask import Flask
from flask import Flask, render_template
from apis import api

app = Flask(__name__)
api.init_app(app)

from view import view_bp
app.register_blueprint(view_bp)

# @app.route('/')
# def view():
#     return render_template('view.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)