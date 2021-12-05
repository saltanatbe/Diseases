from flask import Blueprint, render_template, request, flash
from sqlalchemy import inspect
from . import db
from .models import Record, Country, Disease

crud = Blueprint('crud', __name__)


@crud.route('/tables', methods=['GET', 'POST'])
def tables():
    table = db.session.query(Record).all()
    return render_template("tables.html", table=table)


@crud.route('/update', methods=['GET', 'POST'])
def update(): 
    if request.method == 'POST':
        email = request.form.get('email')
        cname = request.form.get('country')
        disease_code = request.form.get('disease_code')
        total_deaths = request.form.get('total_deaths')
        total_patients = request.form.get('total_patients')
        
        if not email or not cname or not disease_code:
            flash('Please, fill all required fields', category='error')
        else:
            updatable = Record.query.filter_by(email=email).filter_by(cname=cname).filter_by(disease_code=disease_code).first()
            
            if updatable:
                if total_deaths!='':
                    updatable.total_deaths = total_deaths
                if total_patients!='':
                    updatable.total_patients = total_patients
                db.session.add(updatable)
                db.session.commit()
                flash('Record was inserted', category='success')
            else:
                flash('There is no such record, please enter again', category='error')
                
    country = str(Country.query.all())[9:-2].split('>, <Country ')
    disease = str(Disease.query.all())[9:-2].split('>, <Disease ')
    return render_template("update.html", country = country, disease = disease)


@crud.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        email = request.form.get('email')
        cname = str(request.form.get('country'))
        disease_code = str(request.form.get('disease_code'))
        total_deaths = request.form.get('total_deaths')
        total_patients = request.form.get('total_patients')

        if not email or not cname or not disease_code:
            flash('Please, fill all required fields', category='error')
        else:    
            record = Record(email=email, cname=cname, disease_code=disease_code, total_deaths=total_deaths, total_patients=total_patients)
            db.session.add(record)
            db.session.commit()
            flash('Record was inserted', category='success')
    country = str(Country.query.all())[9:-2].split('>, <Country ')
    disease = str(Disease.query.all())[9:-2].split('>, <Disease ')
    return render_template("insert.html", country = country, disease = disease)


@crud.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        email = request.form.get('email')
        cname = str(request.form.get('country'))
        disease_code = str(request.form.get('disease_code'))
        
        if not email or not cname or not disease_code:
            flash('Please, fill all required fields', category='error')
        else:
            delete_this = Record.query.filter_by(email=email).filter_by(cname=cname).filter_by(disease_code=disease_code).first()
            if delete_this:
                db.session.delete(delete_this)
                db.session.commit()
                flash('Record was deleted', category='success')
            else:
                flash('There is no such record, please enter again', category='error')
    country = str(Country.query.all())[9:-2].split('>, <Country ')
    disease = str(Disease.query.all())[9:-2].split('>, <Disease ')
    return render_template("delete.html", country=country, disease=disease)