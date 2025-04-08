import dbconfig
from dbconfig import db

with dbconfig.app_context():
    db.create_all()
