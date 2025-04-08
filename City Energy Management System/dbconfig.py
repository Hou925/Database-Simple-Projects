# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def init_app(app):
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@10.30.123.123/demo'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hou210297@localhost:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
