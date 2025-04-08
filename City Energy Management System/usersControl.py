from flask import render_template,request,redirect,url_for,Blueprint
from dbconfig import db
from models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        age = request.form['age']
        new_user = User(username=username, password=password, gender=gender, age = age)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_user.html')

@users_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edituser(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.gender = request.form['gender']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edituser.html', user=user)

@users_bp.route('/delete/<int:user_id>', methods=['GET', 'POST'])
def deleteuser(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))
