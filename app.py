from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

# from security import authenticate, identity
from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.secret_key = 'mont-hin-gha-and-pizza'
app.config['JWT_SECRET_KEY'] = 'mont-hin-gha-and-pizza'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config['JWT_HEADER_TYPE'] = ''
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
