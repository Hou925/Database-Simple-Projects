from dbconfig import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    gender = db.Column(db.String(2),  nullable=False)
    password = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)

class EnergyType(db.Model):
    __tablename__ = 'EnergyType'
    EnergyID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EnergyName = db.Column(db.String(50))

class Area(db.Model):
    __tablename__ = 'Area'
    AreaID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AreaName = db.Column(db.String(50))

class EnergyDevice(db.Model):
    __tablename__ = 'EnergyDevice'
    DeviceID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AreaID = db.Column(db.Integer)
    EnergyID = db.Column(db.Integer)