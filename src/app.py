"""
This is a main function of TODO app.
"""
from flask import Flask
from apis import api

# import blueprints
from view import view_bp

app = Flask(__name__)
api.init_app(app)

app.register_blueprint(view_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
