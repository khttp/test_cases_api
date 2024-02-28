from flask import Flask
from models.model import db
from routes.test_case import  api
from routes.test_asset import  asset_api
from routes.test_results import  result_api

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_cases.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(api)
    app.register_blueprint(asset_api)
    app.register_blueprint(result_api)
    with app.app_context():
        db.create_all()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
