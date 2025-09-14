from flask import Blueprint,request,jsonify
from models.models import db,Users
from datetime import date
from flask_jwt_extended import create_access_token

user_bp=Blueprint("auth",__name__)

@user_bp.route("/register",methods=['POST'])
def register_user():
    data=request.get_json()

    if Users.query.filter_by(username=data["username"]).first():
        return jsonify({"message":"User already exists"}),400
    
    user=Users(username=data["username"],password=data["password"],role=data["role"],created_on=date.today())
    db.session.add(user)
    db.session.commit()
    return jsonify({"message":"User added successfully","user_id":user.username}),201

from flask_jwt_extended import create_access_token

@user_bp.route("/login", methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = Users.query.filter_by(username=username).first()
    if user and user.password == password:
        access_token = (create_access_token(identity=str({
            "username": user.username,
            "role": user.role
        })))
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Wrong credentials"}), 401
