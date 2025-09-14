from flask import Blueprint, request, jsonify
from models.models import db, Patients
from datetime import date
from flask_jwt_extended import jwt_required

patient_bp = Blueprint("patients", __name__)

@patient_bp.route("/patients", methods=['POST'])
@jwt_required()
def register_patient():
    data = request.get_json()

    new_patient = Patients(
        name=data["name"],
        age=data["age"],
        disease=data["disease"],
        admitted_on=date.today()
    )
    db.session.add(new_patient)
    db.session.commit()

    return jsonify({"message": "Patient registered successfully", "id": new_patient.id}), 201


@patient_bp.route("/patients", methods=['GET'])
@jwt_required()
def get_patients():
    patients = Patients.query.all()
    patient_list = [
        {
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "disease": p.disease,
            "admitted_on": p.admitted_on.strftime("%Y-%m-%d") if p.admitted_on else None
        }
        for p in patients
    ]
    return jsonify(patient_list), 200


@patient_bp.route("/patients/disease/<disease>", methods=['GET'])
@jwt_required()
def get_patients_by_disease(disease):
    patients = Patients.query.filter_by(disease=disease).all()
    if not patients:
        return jsonify({"message": f"No patients found with disease {disease}"}), 404

    patient_list = [
        {
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "disease": p.disease
        }
        for p in patients
    ]
    return jsonify(patient_list), 200


@patient_bp.route("/patients/search", methods=['GET'])
@jwt_required()
def search_patient():
    name = request.args.get("name")
    if not name:
        return jsonify({"message": "Please provide a name to search"}), 400

    patients = Patients.query.filter(Patients.name.ilike(f"%{name}%")).all()
    if not patients:
        return jsonify({"message": "No patients found"}), 404

    patient_list = [
        {
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "disease": p.disease
        }
        for p in patients
    ]
    return jsonify(patient_list), 200


@patient_bp.route("/patients/<int:id>", methods=['PUT'])
@jwt_required()
def update_patient(id):
    patient = Patients.query.get(id)
    if not patient:
        return jsonify({"message": "Patient not found"}), 404

    data = request.get_json()
    patient.name = data.get("name", patient.name)
    patient.age = data.get("age", patient.age)
    patient.disease = data.get("disease", patient.disease)

    db.session.commit()
    return jsonify({"message": "Patient updated successfully"}), 200


@patient_bp.route("/patients/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_patient(id):
    patient = Patients.query.get(id)
    if not patient:
        return jsonify({"message": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient deleted successfully"}), 200
