from flask import Blueprint, jsonify, request
from ..db.models import User, Book, Transaction
from mongoengine.queryset.visitor import Q

# define the blueprint
user_blueprint = Blueprint(name="user_blueprint", import_name=__name__)

# note: global variables can be accessed from view functions


# create user
@user_blueprint.route('/create-user', methods=['POST'])
def create_user():
    try:
        req = request.get_json()
        user = User(name=req['name'], email=req['email'], password=req['password'])
        user.save()
        data = {"message":"User created!", "username":req['name']}
    except Exception as e:
        data = {"message":"request failed!",
                "request":"GET",
                "parameters help":"username + email + password",
                "parameters required":'/{"username":"example", "email":"example@gmail.com", "password":"example/}',
                "exception":e}
    return jsonify(data)

