from flask import Blueprint, request, jsonify
from models.models import db, Departments,Users
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

department_bp = Blueprint("dept", __name__)

@department_bp.route("/add", methods=['POST'])
@jwt_required()
def add_department():
    current_user = get_jwt_identity()   
    user_role = current_user.get("role") 

    if user_role not in ["admin", "staff"]:
        return jsonify({"message": "You are not authorized to add departments"}), 403

    data = request.get_json()
    if Departments.query.filter_by(name=data["name"]).first():
        return jsonify({"message": "Department already found"}), 400

    department = Departments(
        name=data["name"],
        head_doctor=data["head_doctor"],
        created_on=date.today()
    )
    db.session.add(department)
    db.session.commit()

    return jsonify({"message": "Department added successfully"}), 201


@department_bp.route("/all", methods=['GET'])
@jwt_required()
def get_all_departments():
    departments = Departments.query.all()
    department_list = [
        {
            "id": dept.id,
            "name": dept.name,
            "head_doctor": dept.head_doctor,
            "created_on": dept.created_on.strftime("%Y-%m-%d") if dept.created_on else None
        }
        for dept in departments
    ]

    return jsonify(department_list), 200
    