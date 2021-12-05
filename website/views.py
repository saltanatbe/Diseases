from flask import Blueprint, render_template, request, flash, redirect
from .models import Disease, DiseaseType
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    disease = []
    disease_code = request.form.get('disease_code')
    pathogen = request.form.get('pathogen')
    description = request.form.get('description')
    id = request.form.get('id')
    if disease_code or pathogen or description or id :
        disease = db.session.query(Disease)
    if disease_code:
        disease = disease.filter_by(disease_code=disease_code)
    if pathogen:
        disease = disease.filter_by(pathogen=pathogen)
    if description:
        disease = disease.filter_by(description=description)
    if id:
        disease = disease.filter_by(id=id)
    diseases = db.session.query(Disease).all()
    return render_template("home.html", disease=disease, diseases=diseases)
       
    

