from flask import Flask,request,jsonify
from config import Config
from models.models import db
from routes.user_route import user_bp
from routes.department_route import department_bp
from routes.patient_route import patient_bp
from flask_jwt_extended import JWTManager


app=Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

jwt=JWTManager(app)

app.register_blueprint(user_bp)
app.register_blueprint(department_bp)
app.register_blueprint(patient_bp)

if (__name__)=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)