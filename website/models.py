from sqlalchemy.sql.schema import PrimaryKeyConstraint
from . import db
from flask_login import UserMixin

class Record(db.Model):
    __tablename__ = 'record'
    email = db.Column(db.String(60), primary_key=True)
    cname = db.Column(db.String(50), primary_key = True)
    
    disease_code = db.Column('disease code', db.String(50), db.ForeignKey('disease.disease code'), primary_key = True)
    total_deaths = db.Column('total deaths', db.Integer)
    total_patients = db.Column('total patients', db.Integer)

    def __repr__(self):
        return "<{}:{}>".format(id, self.email)

class Country(db.Model):
    __tablename__ = 'country'
    cname = db.Column(db.String(50), primary_key=True)
    population = db.Column(db.BigInteger)

class DiseaseType(db.Model):
    __tablename__='diseasetype'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140))


class Disease(db.Model):
    __tablename__='disease'
    disease_code = db.Column('disease code', db.String, primary_key=True)
    pathogen = db.Column(db.String)
    description = db.Column(db.String)
    id = db.Column(db.Integer, db.ForeignKey('diseasetype.id'))
    diseasetype = db.relationship('DiseaseType')
   

class Discover(db.Model):
    __tablename__='discover'
    cname = db.Column(db.String(50), db.ForeignKey('country.cname'))
    disease_code = db.Column('disease code', db.String, primary_key=True)
    first_enc_date = db.Column('first enc date', db.String)
    country = db.relationship('Country')

class User(db.Model):
    __tablename__='User'
    email = db.Column(db.String(60), unique=True, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    salary = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    cname = db.Column(db.String(50), db.ForeignKey('country.cname'))
    country = db.relationship('Country')

class PublicServant(db.Model):
    __tablename__='publicservant'
    email = db.Column(db.String(60), db.ForeignKey('User.email'), primary_key=True)
    department = db.Column(db.String(50))
    user = db.relationship('User')

class Doctor(db.Model):
    __tablename__='doctor'
    email = db.Column(db.String(60), db.ForeignKey('User.email'), primary_key=True)
    degree = db.Column(db.String(20))
    user = db.relationship('User')

class Specialize(db.Model):
    __tablename__='specialize'
    id = db.Column(db.Integer, db.ForeignKey('diseasetype.id'), primary_key=True)
    email = db.Column(db.String(60), db.ForeignKey('doctor.email'), primary_key=True)
    diseasetype = db.relationship('DiseaseType')
    doctor = db.relationship('Doctor')
    